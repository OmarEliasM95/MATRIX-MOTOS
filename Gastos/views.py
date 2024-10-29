from django.shortcuts import render,redirect
from .models import *
from Empleados import *
from .forms import *
from django.contrib.auth.decorators import login_required
@login_required
def gasto_panel(request):
    formulario=Formulario_Gasto()
    lista_gasto=Gasto.objects.filter(id_sesion=request.session.session_key)
    return render(request, 'gasto.html', {'formulario':formulario, 'lista_gasto':lista_gasto})
def agregar_gasto(request):
    if request.method == 'POST':
        formulario=Formulario_Gasto(request.POST)
        if formulario.is_valid():
            formulario.instance.id_sesion=request.session.session_key
            formulario.instance.empleado=Empleado.objects.get(username=request.user.username)
            formulario.save()
    return redirect('gasto_panel')