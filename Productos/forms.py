from .models import *
from django import forms
from django.forms import ModelForm

class formulario_producto(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'