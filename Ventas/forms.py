from .models import *
from django.forms import ModelForm
class Formulario_Pago(ModelForm):
    class Meta:
        model = Venta
        fields=['metodo_pago']
        labels={'metodo_pago':'Metodos de Pago'}
        