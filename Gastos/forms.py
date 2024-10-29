from django.forms import ModelForm
from .models import *
class Formulario_Gasto(ModelForm):
    class Meta:
        model = Gasto
        fields = ['descripcion_gasto','costo']