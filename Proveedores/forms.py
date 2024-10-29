from .models import *
from django.forms import ModelForm
class formulario_proveedor(ModelForm):
    class Meta:
        model= Proveedor
        fields= '__all__'