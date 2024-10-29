from django.shortcuts import render, redirect
from .forms import *
from .models import Empleado, Caja
from Ventas.models import *
from Compras.models import *
from Gastos.models import *
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.db.models import Sum

def obtener_caja_abierta(user):
    return Caja.objects.filter(empleado__username=user.username, estado='Abierta').first()

@login_required
def apertura_view(request):
    caja_abierta = obtener_caja_abierta(request.user)
    if caja_abierta:
        request.session['caja_abierta'] = True
        request.session['empleado'] = caja_abierta.empleado.username
        request.session['fecha_apertura'] = caja_abierta.fecha_apertura.strftime("%Y-%m-%d %H:%M:%S")
        return redirect('cierre')

    if request.method == 'GET':
        formulario_apertura = apertura()
        return render(request, 'apertura.html', {'formulario_apertura': formulario_apertura})

    if request.method == 'POST':
        formulario_apertura = apertura(request.POST)
        formulario_apertura.instance.empleado = Empleado.objects.get(username=request.user.username)
        if formulario_apertura.is_valid():
            formulario_apertura.instance.estado = 'Abierta'
            formulario_apertura.save()
            request.session['caja_abierta'] = True
            request.session['empleado'] = formulario_apertura.instance.empleado.username
            request.session['fecha_apertura'] = formulario_apertura.instance.fecha_apertura.strftime("%Y-%m-%d %H:%M:%S")
            return redirect('menu')
        return render(request, 'apertura.html', {'formulario_apertura': formulario_apertura})

@login_required
def cierre_view(request):
    caja_abierta = obtener_caja_abierta(request.user)
    if not caja_abierta:
        request.session['caja_abierta'] = False
        return redirect('apertura')

    id_sesion = request.session.session_key
    lista_ventas = Venta.objects.filter(id_sesion=id_sesion)
    total_ventas = sum(venta.total_venta for venta in lista_ventas)

    ventas_efectivo = sum(venta.total_venta for venta in lista_ventas if venta.metodo_pago == 'Efectivo')
    ventas_transferencia = sum(venta.total_venta for venta in lista_ventas if venta.metodo_pago == 'Transferencia')
    ventas_tarjeta_credito = sum(venta.total_venta for venta in lista_ventas if venta.metodo_pago == 'Tarjeta_de_Credito')
    ventas_tarjeta_debito = sum(venta.total_venta for venta in lista_ventas if venta.metodo_pago == 'Tarjeta_de_Debito')

    lista_compras = Compra.objects.filter(id_sesion=id_sesion)
    total_compras = sum(compra.total for compra in lista_compras)
    compras_efectivo = sum(compra.total for compra in lista_compras if compra.metodo_pago == 'Efectivo')
    compras_transferencia = sum(compra.total for compra in lista_compras if compra.metodo_pago == 'Transferencia')
    compras_tarjeta_debito = sum(compra.total for compra in lista_compras if compra.metodo_pago == 'Tarjeta_de_Debito')

    lista_gastos = Gasto.objects.filter(id_sesion=id_sesion)
    gastos_compra = sum(gasto.costo for gasto in lista_gastos)

    lista_dinero = Dinero.objects.filter(id_sesion=id_sesion)
    dinero_ingreso = sum(dinero.ing_egre for dinero in lista_dinero if dinero.tipo_dinero == 'Ingreso')
    dinero_egreso = sum(dinero.ing_egre for dinero in lista_dinero if dinero.tipo_dinero == 'Egreso')

    total_ingresos = dinero_ingreso + total_ventas
    total_egresos = total_compras + gastos_compra + dinero_egreso

    saldo_final = total_ventas + caja_abierta.saldo_inicial + dinero_ingreso - total_egresos
    formulario_cierre = cierre(instance=caja_abierta)
    fecha_actual = datetime.now()

    if request.method == 'GET':
        return render(request, 'cierre.html', {
            'formulario_cierre': formulario_cierre,
            'total_ventas': total_ventas,
            'ventas_efectivo': ventas_efectivo,
            'ventas_transferencia': ventas_transferencia,
            'ventas_tarjeta_credito': ventas_tarjeta_credito,
            'ventas_tarjeta_debito': ventas_tarjeta_debito,
            'total_compras': total_compras,
            'compras_transferencia': compras_transferencia,
            'compras_efectivo': compras_efectivo,
            'compras_tarjeta_debito': compras_tarjeta_debito,
            'gastos_compra': gastos_compra,
            'saldo_final': saldo_final,
            'dinero_ingreso': dinero_ingreso,
            'dinero_egreso': dinero_egreso,
            'fecha_actual': fecha_actual,
            'total_egresos': total_egresos,
            'total_ingresos': total_ingresos,
            'caja_abierta': caja_abierta
        })

    if request.method == 'POST':
        caja_abierta.fecha_cierre = datetime.now()
        caja_abierta.estado = 'Cerrada'
        caja_abierta.saldo_final = saldo_final 
        caja_abierta.save()
        request.session['caja_abierta'] = False
        return redirect('menu')

@login_required
def panel_dinero(request):
    formulario = formulario_dinero()
    tipo = request.GET.get('tipo')
    user=request.user
    id_sesion_actual = request.session.session_key
    lista_dinero=[]

    if tipo == 'ingreso':
        lista_dinero = Dinero.objects.filter(tipo_dinero='Ingreso', empleado=user,id_sesion=id_sesion_actual)
    elif tipo == 'egreso':
        lista_dinero = Dinero.objects.filter(tipo_dinero='Egreso', empleado=user,id_sesion=id_sesion_actual)
    elif tipo=='todos':
        lista_dinero = Dinero.objects.filter(empleado=user,id_sesion=id_sesion_actual)
    return render(request, 'panel_iye.html', {'formulario': formulario, 'lista_dinero': lista_dinero})

def agregar_dinero(request):
    if request.method == 'POST':
        formulario = formulario_dinero(request.POST)
        if formulario.is_valid():
            formulario.instance.id_sesion = request.session.session_key
            formulario.instance.empleado = Empleado.objects.get(username=request.user.username)
            formulario.save()
    return redirect('panel_dinero')

def datos_caja(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    mes = request.GET.get('mes')
    anio = request.GET.get('anio')

    meses = list(range(1, 13))  
    anios = list(range(2024, 2051))  

    ventas = 0
    compras = 0
    gastos = 0
    ingresos = 0
    egresos = 0
    valuesPeriodo = []
    
    if fecha_inicio and fecha_fin:
        fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        
        valuesPeriodo = [(fecha_inicio + timedelta(days=x)).strftime('%Y-%m-%d') for x in range((fecha_fin - fecha_inicio).days + 1)]
        
        ventas = Venta.objects.filter(fecha__range=[fecha_inicio, fecha_fin]).aggregate(total=Sum('total_venta'))['total'] or 0
        compras = Compra.objects.filter(fecha_compra__range=[fecha_inicio, fecha_fin]).aggregate(total=Sum('total'))['total'] or 0
        gastos = Gasto.objects.filter(fecha__range=[fecha_inicio, fecha_fin]).aggregate(total=Sum('costo'))['total'] or 0 
        ingresos = Dinero.objects.filter(
            fecha_dinero__range=[fecha_inicio, fecha_fin], tipo_dinero='Ingreso'
        ).aggregate(total=Sum('ing_egre'))['total'] or 0
        egresos = Dinero.objects.filter(
            fecha_dinero__range=[fecha_inicio, fecha_fin], tipo_dinero='Egreso'
        ).aggregate(total=Sum('ing_egre'))['total'] or 0

    elif mes:
        mes = int(mes) if mes else datetime.now().month
        anio = int(anio) if anio else datetime.now().year

        ventas = Venta.objects.filter(fecha__month=mes, fecha__year=anio).aggregate(total=Sum('total_venta'))['total'] or 0
        compras = Compra.objects.filter(fecha_compra__month=mes, fecha_compra__year=anio).aggregate(total=Sum('total'))['total'] or 0
        gastos = Gasto.objects.filter(fecha__month=mes, fecha__year=anio).aggregate(total=Sum('costo'))['total'] or 0  
        ingresos = Dinero.objects.filter(
            fecha_dinero__month=mes, fecha_dinero__year=anio, tipo_dinero='Ingreso'
        ).aggregate(total=Sum('ing_egre'))['total'] or 0
        egresos = Dinero.objects.filter(
            fecha_dinero__month=mes, fecha_dinero__year=anio, tipo_dinero='Egreso'
        ).aggregate(total=Sum('ing_egre'))['total'] or 0

    return render(request, 'grafico.html', {
        'ventas': ventas,
        'compras': compras,
        'gastos': gastos,
        'ingresos': ingresos,
        'egresos': egresos,
        'valuesPeriodo': valuesPeriodo,
        'meses': meses,
        'anios': anios,
    })
