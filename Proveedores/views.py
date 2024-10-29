from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator 

def agregar_proveedor(request):
    proveedor_agregar=formulario_proveedor(request.POST)
    if proveedor_agregar.is_valid():
        proveedor_agregar.save()
    return redirect('panel_proveedores')
@login_required
def panel_proveedores(request):
    listado = Proveedor.objects.all()
    paginator=Paginator(listado,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    mostrar_formulario = formulario_proveedor()
    busqueda= request.GET.get('busqueda','')
    if busqueda:
        listado=listado.filter(
            Q(nombre__icontains=busqueda)

        )
    return render(request, 'proveedores.html', {'listado':listado, 'mostrar_formulario':mostrar_formulario,'page_obj':page_obj})
def eliminar_proveedor(request, id_proveedor):
    proveedor_buscado=Proveedor.objects.get(id=id_proveedor)
    proveedor_buscado.delete()
    return redirect('panel_proveedores')
def editar_proveedor(request, id_proveedor):
    proveedor_buscado=Proveedor.objects.get(id=id_proveedor)
    if request.method == 'GET':
        formulario_editar=formulario_proveedor(instance=proveedor_buscado)
        return render(request, 'editar_proveedor.html', {'formulario_editar':formulario_editar, 'id_proveedor':id_proveedor})
    if request.method == 'POST':
        formulario_editar=formulario_proveedor(request.POST, instance=proveedor_buscado)
        if formulario_editar.is_valid():
            formulario_editar.save()
            return redirect('panel_proveedores')      