from .models import *
from django.forms import ModelForm

class apertura(ModelForm):
    class Meta:
        model=Caja
        fields = ['saldo_inicial']

class cierre(ModelForm):
    class Meta:
        model = Caja
        fields = '__all__'
class formulario_dinero(ModelForm):
    class Meta:
        model = Dinero
        fields = ['ing_egre','tipo_dinero']