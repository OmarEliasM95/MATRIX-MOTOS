from django.shortcuts import render, redirect
from .models import *
from .forms import formulario_producto
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def agregar_producto(request):
    producto_agregar=formulario_producto(request.POST)
    if producto_agregar.is_valid():
        producto_agregar.save()
    return redirect('lista_producto')
@login_required
def lista_producto(request):
    listado=Producto_Intermedia.objects.all().order_by('producto__nombre')
    paginator=Paginator(listado,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    mostrar_formulario = formulario_producto()
    return render(request, 'productos.html', {'listado':listado, 'mostrar_formulario':mostrar_formulario,'page_obj':page_obj})
def eliminar_producto(request, id_producto):
    producto_buscado=Producto.objects.get(id=id_producto)
    producto_buscado.delete()
    return redirect('lista_producto')
def editar_producto(request, id_producto):
    producto_buscado=Producto.objects.get(id=id_producto)
    if request.method == 'GET':
        formulario_editar=formulario_producto(instance=producto_buscado)
        return render(request, 'editar_producto.html', {'formulario_editar':formulario_editar, 'id_producto':id_producto})
    if request.method == 'POST':
        formulario_editar=formulario_producto(request.POST, instance=producto_buscado)
        if formulario_editar.is_valid():
            formulario_editar.save()
            return redirect('lista_producto')