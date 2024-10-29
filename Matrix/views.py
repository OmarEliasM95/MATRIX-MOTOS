from django.shortcuts import render,redirect
from Compras.models import *
from Productos.models import *
from Ventas.models import *
from Gastos.models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator

def error_400(request, exception):
    if settings.DEBUG:
        return render(request, '400.html', status=400)
    return render(request, '400.html', status=400)

def error_403(request, exception):
    if settings.DEBUG:
        return render(request, '403.html', status=403)
    return render(request, '403.html', status=403)

def error_404(request, exception):
    if settings.DEBUG:
        return render(request, '404.html', status=404)
    return render(request, '404.html', status=404)

def error_500(request):
    if settings.DEBUG:
        return render(request, '500.html', status=500)
    return render(request, '500.html', status=500)

@login_required
def menu(request):
    caja_abierta = Caja.objects.filter(empleado=request.user, estado='Abierta').first()
    if caja_abierta:  
        fecha_apertura = caja_abierta.fecha_apertura  
        empleado = caja_abierta.empleado 
    else:
        fecha_apertura = None
        empleado = None
    return render(request, 'ingreso.html', {
        'caja_abierta': caja_abierta,  
        'fecha_apertura': fecha_apertura,
        'empleado': empleado 
    })
@login_required
def historial_compras(request):
    historial_compras=Compra.objects.all()
    paginator= Paginator(historial_compras,10)
    page_number=request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    return render(request,'historial_compras.html', {'historial_compras':historial_compras,'page_obj':page_obj})
def ver_detalle_compra(request, id_compras):
    compra=Compra.objects.get(id=id_compras)
    producto_comprados=compra.compra_intermedio_set.all()
    return render(request,'ver_detalle_compra.html', {'productos_comprados':producto_comprados})
@login_required
def historial_ventas(request):
    historial_ventas=Venta.objects.all()
    paginator=Paginator(historial_ventas,10)
    page_number=request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    return render(request,'historial_ventas.html',{'historial_ventas':historial_ventas,'page_obj':page_obj})
def ver_detalle_venta(request, id_ventas):
    venta=Venta.objects.get(id=id_ventas)
    productos_vendidos=venta.productos_vendidos_set.all()
    return render(request,'ver_detalle_venta.html',{'productos_vendidos':productos_vendidos})
@login_required
def panel_historial(request):
    return render(request,'historiales.html')