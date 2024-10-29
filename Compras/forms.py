from .models import *
from django.forms import ModelForm

class Formulario_Compra(ModelForm):
    class Meta:
        model=Compra
        fields=['proveedor', 'metodo_pago']
class FormularioProductoComprado(ModelForm):
    class Meta:
        model=Compra_intermedio
        fields=['precio_de_compra', 'cantidad']