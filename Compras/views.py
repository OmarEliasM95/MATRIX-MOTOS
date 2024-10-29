from django.shortcuts import render, redirect
from .models import *
from Productos.models import *
from Proveedores.models import *
from Empleados.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Count
from datetime import datetime, timedelta


@login_required
def panel_compras(request):
    id_proveedor=request.session.get('id_proveedor', None)
    if not Compra.objects.exists():
         request.session.pop('id_compra', None)
    id_compra=request.session.get('id_compra', None)

    if id_proveedor:
        proveedor=Proveedor.objects.get(id=id_proveedor)
        nombre_proveedor=proveedor.nombre
        formulario_compra=Formulario_Compra({'proveedor':id_proveedor})
        if formulario_compra.is_valid():
            lista_productos_proveedor=Producto_Intermedia.objects.filter(proveedor=proveedor)
            contexto=({'formulario_compra':formulario_compra, 'lista_productos_proveedor':lista_productos_proveedor,'nombre_proveedor':nombre_proveedor })
  
    else:
        formulario_compra=Formulario_Compra()
        contexto=({'formulario_compra':formulario_compra})

    if id_compra:
        compra=Compra.objects.last()
        if id_compra == compra.id:
            lista_compra=compra.compra_intermedio_set.all()
            if lista_compra:
                total_compra=sum(producto.precio_de_compra for producto in lista_compra)
                compra.total=total_compra
                compra.save()
                contexto.update({'compra':compra, 'lista_compra':lista_compra})
            else: 
                compra.delete()
    formulario_comprado=FormularioProductoComprado()
    compra_sesion=Compra.objects.filter(id_sesion=request.session.session_key)
    contexto.update({'formulario_comprado':formulario_comprado,'compra_sesion':compra_sesion})
    return render(request, 'compras.html', contexto)

def seleccionar_proveedor(request):
    if request.method=='POST':
        proveedor_seleccionado=Formulario_Compra(request.POST)
        if proveedor_seleccionado.is_valid():
            id_proveedor= proveedor_seleccionado.instance.proveedor.id
            request.session['id_proveedor']=id_proveedor
            return redirect('panel_compras')

def agregar_producto_compra(request, id_producto):
    producto=Producto.objects.get(id=id_producto)
    id_compra=request.session.get('id_compra', None)

    if id_compra:
        try:
            compra=Compra.objects.get(id=id_compra)
        except:
            compra=Compra(id=id_compra)
            proveedor=Proveedor.objects.get(id=request.session.get('id_proveedor'))
            compra.proveedor=proveedor
            compra.save()
    else:
        compra=Compra()
        id_proveedor=request.session.get('id_proveedor', None)
        proveedor=Proveedor.objects.get(id=id_proveedor)
        compra.proveedor=proveedor
        compra.id=id_compra
        compra.save()
        request.session['id_compra']=compra.id
  
    if request.method=='POST':
        formulario_agregar=FormularioProductoComprado(request.POST)
        formulario_agregar.instance.producto = producto
        formulario_agregar.instance.compra = compra
        if formulario_agregar.is_valid():
            formulario_agregar.save()
        return redirect('panel_compras')

def eliminar_producto_compra(request, id_producto):
    id_compra=request.session.get('id_compra')
    producto_compra_a_eliminar=Compra_intermedio.objects.get(compra_id=id_compra, producto_id=id_producto)
    producto_compra_a_eliminar.delete()
    return redirect('panel_compras')

def confirmar_compra(request):
    if request.method=='POST':
        id_compra=request.session.get('id_compra')
        compra=Compra.objects.get(id=id_compra)
        formulario_compra=Formulario_Compra(request.POST)
        if formulario_compra.is_valid():
            metodo_pago=formulario_compra.cleaned_data['metodo_pago']
            compra.metodo_pago=metodo_pago
            compra.empleado=Empleado.objects.get(username=request.user.username)
            compra.id_sesion=request.session.session_key
            compra.save()
            request.session.pop('id_compra')
            request.session.pop('id_proveedor')
        lista_productos_comprados=compra.compra_intermedio_set.all()
        for producto_comprado in lista_productos_comprados:
            producto=Producto.objects.get(id=producto_comprado.producto.id)
            producto.existencias+=producto_comprado.cantidad
            producto.save()
        return redirect('panel_compras' )
    
def grafico_compras(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    mes = request.GET.get('mes')
    anio = request.GET.get('anio') or datetime.now().year

    meses = list(range(1, 13))  
    anios = list(range(2024, 2051))  

    total_efectivo = 0
    total_transferencia = 0
    total_tarjeta_debito = 0
    periodo = []
    
    if fecha_inicio and fecha_fin:
        fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')

        periodo = [(fecha_inicio + timedelta(days=x)).strftime('%Y-%m-%d') for x in range((fecha_fin - fecha_inicio).days + 1)]

        compras = Compra.objects.filter(fecha_compra__range=[fecha_inicio, fecha_fin])
        total_efectivo = int(compras.filter(metodo_pago='Efectivo').aggregate(total=Sum('total'))['total'] or 0)
        total_transferencia = int(compras.filter(metodo_pago='Transferencia').aggregate(total=Sum('total'))['total'] or 0)
        total_tarjeta_debito = int(compras.filter(metodo_pago='Tarjeta_de_Debito').aggregate(total=Sum('total'))['total'] or 0)

    elif mes:
        mes = int(mes) 
        anio = int(anio)

        periodo=[f"{anio}-{mes:02d}"]
        compras = Compra.objects.filter(fecha_compra__year=anio, fecha_compra__month=mes)
        total_efectivo = int(compras.filter(metodo_pago='Efectivo').aggregate(total=Sum('total'))['total'] or 0)
        total_transferencia = int(compras.filter(metodo_pago='Transferencia').aggregate(total=Sum('total'))['total'] or 0)
        total_tarjeta_debito = int(compras.filter(metodo_pago='Tarjeta_de_Debito').aggregate(total=Sum('total'))['total'] or 0)

    elif anio:
        anio = int(anio)
        periodo = [str(anio)]

        compras = Compra.objects.filter(fecha_compra__year=anio)
        total_efectivo = int(compras.filter(metodo_pago='Efectivo').aggregate(total=Sum('total'))['total'] or 0)
        total_transferencia = int(compras.filter(metodo_pago='Transferencia').aggregate(total=Sum('total'))['total'] or 0)
        total_tarjeta_debito = int(compras.filter(metodo_pago='Tarjeta_de_Debito').aggregate(total=Sum('total'))['total'] or 0)

    context = {
        'total_efectivo_compra': total_efectivo,
        'total_transferencia_compra': total_transferencia,
        'total_tarjeta_debito_compra': total_tarjeta_debito,
        'periodo': periodo,
        'meses': meses,
        'anios': anios,
        'mes': mes,
        'anio': anio
    }

    return render(request, 'grafico_compras.html', context)