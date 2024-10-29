from django.shortcuts import render, redirect
from Productos.models import *
from Empleados.models import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import timedelta, datetime

@login_required
def panel_venta(request):
    lista_producto=Producto.objects.all()
    if not Venta.objects.exists():
        venta=Venta.objects.create()
        request.session['id_venta']=venta.id
        productos=venta.productos_vendidos_set.all()
        venta.total_venta=0
        for producto in productos:
            venta.total_venta+=producto.subtotal
        formularioP=Formulario_Pago()
        venta.save()
    else:
        venta=Venta.objects.last()
        request.session['id_venta']=venta.id
        productos=venta.productos_vendidos_set.all()
        venta.total_venta=0
        for producto in productos:
            venta.total_venta+=producto.subtotal
        formularioP=Formulario_Pago()
        venta.save()
    return render(request,'ventas.html', {'lista_producto':lista_producto, 'venta':venta,
                                         'productos':productos, 'formularioP':formularioP})
def agregar_producto(request,id_producto):
    id_venta=request.session.get('id_venta')
    venta=Venta.objects.get(id=id_venta)
    if request.method == 'POST':
        prod_vendidos=Producto.objects.get(id=id_producto)
        cantidad=int(request.POST.get('cantidad'))
        if Productos_Vendidos.objects.filter(venta=venta, producto=prod_vendidos).exists():
            new_producto=Productos_Vendidos.objects.get(venta=venta, producto=prod_vendidos)
            new_producto.cantidad+=cantidad
            new_producto.subtotal=new_producto.cantidad*prod_vendidos.precio
            new_producto.save()
        else:
            subtotal=prod_vendidos.precio*cantidad
            venta.productos.add(prod_vendidos,through_defaults={'cantidad':cantidad,'subtotal':subtotal})
        prod_vendidos.existencias-=cantidad
        prod_vendidos.save()
    return redirect('panel_venta')

def eliminar_producto_vendido(request, id_producto):
    id_venta=request.session.get('id_venta')
    venta=Venta.objects.get(id=id_venta)
    producto_a_eliminar=Producto.objects.get(id=id_producto)
    cantidad_eliminada=venta.productos_vendidos_set.get(producto=producto_a_eliminar).cantidad
    venta.productos.remove(producto_a_eliminar)
    producto_a_eliminar.existencias+=cantidad_eliminada
    producto_a_eliminar.save()
    return redirect('panel_venta')

def crear_factura(request, id_venta):
    venta=Venta.objects.get(id=id_venta)
    if request.method == 'POST':
        formularioP=Formulario_Pago(request.POST, instance=venta)
        if formularioP.is_valid():
            formularioP.save()
    venta.fecha=datetime.now()
    venta.empleado=Empleado.objects.get(username=request.user.username)
    venta.id_sesion=request.session.session_key
    venta.save()
    productos_a_vender=venta.productos_vendidos_set.all()
    return render(request,'factura.html',{'venta':venta,'productos_a_vender':productos_a_vender})
def nueva_venta(request):
    venta=Venta.objects.create()
    return redirect('panel_venta')

def grafico_ventas(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    mes = request.GET.get('mes')
    anio = request.GET.get('año') or datetime.now().year
    
    meses=list(range(1,13))
    anios=list(range(2024,2051))

    efectivo_vta= 0
    transferencia_vta=0
    tarjeta_debito_vta=0
    tarjeta_credito_vta=0
    periodoVta= []

    if fecha_inicio and fecha_fin: 
        fecha_inicio=datetime.strptime(fecha_inicio,'%Y-%m-%d')
        fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        
        periodoVta = [(fecha_inicio + timedelta(days=x)).strftime('%Y-%m-%d') for x in range((fecha_fin - fecha_inicio).days + 1)]
        ventas= Venta.objects.filter(fecha__range=[fecha_inicio,fecha_fin])

        efectivo_vta= int(ventas.filter(metodo_pago='Efectivo').aggregate(total=Sum('total_venta'))['total'] or 0)
        transferencia_vta= int(ventas.filter(metodo_pago='Transferencia').aggregate(total=Sum('total_venta'))['total'] or 0)
        tarjeta_debito_vta= int(ventas.filter(metodo_pago='Tarjeta_de_Debito').aggregate(total=Sum('total_venta'))['total'] or 0)
        tarjeta_credito_vta= int(ventas.filter(metodo_pago='Tarjeta_de_Credito').aggregate(total=Sum('total_venta'))['total'] or 0)
        
    elif mes:
        mes=int(mes)
        anio=int(anio)

        periodoVta= [f"{anio}-{mes:02d}"]

        ventas= Venta.objects.filter(fecha__year=anio,fecha__month=mes)

        efectivo_vta= int(ventas.filter(metodo_pago='Efectivo').aggregate(total=Sum('total_venta'))['total'] or 0)
        transferencia_vta= int(ventas.filter(metodo_pago='Transferencia').aggregate(total=Sum('total_venta'))['total'] or 0)
        tarjeta_debito_vta= int(ventas.filter(metodo_pago='Tarjeta_de_Debito').aggregate(total=Sum('total_venta'))['total'] or 0)
        tarjeta_credito_vta= int(ventas.filter(metodo_pago='Tarjeta_de_Credito').aggregate(total=Sum('total_venta'))['total'] or 0)

    elif anio:
        anio= int(anio)
        periodoVta=[str(anio)]

        ventas=Venta.objects.filter(fecha__year=anio)

        efectivo_vta= int(ventas.filter(metodo_pago='Efectivo').aggregate(total=Sum('total_venta'))['total'] or 0)
        transferencia_vta= int(ventas.filter(metodo_pago='Transferencia').aggregate(total=Sum('total_venta'))['total'] or 0)
        tarjeta_debito_vta= int(ventas.filter(metodo_pago='Tarjeta_de_Debito').aggregate(total=Sum('total_venta'))['total'] or 0)
        tarjeta_credito_vta= int(ventas.filter(metodo_pago='Tarjeta_de_Credito').aggregate(total=Sum('total_venta'))['total'] or 0)

    context={
        'periodoVta':periodoVta,
        'efectivo_vta':efectivo_vta,
        'transferencia_vta':transferencia_vta,
        'tarjeta_debito_vta':tarjeta_debito_vta,
        'tarjeta_credito_vta':tarjeta_credito_vta,
        'meses':meses,
        'anios':anios,
        'mes':mes,
        'anio':anio
    }
    return render(request,'grafico_ventas.html',context)