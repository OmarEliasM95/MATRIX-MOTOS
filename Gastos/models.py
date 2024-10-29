from django.db import models
from Empleados.models import Empleado
from datetime import datetime
from django.core.validators import MinValueValidator

class Gasto(models.Model): 
    fecha=models.DateTimeField(default=datetime.now)
    empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE,null=True,blank=True)
    descripcion_gasto=models.CharField(max_length=100, verbose_name= "Descripción",blank=False, null=False)
    costo=models.DecimalField(default=0,max_digits=10, decimal_places=2, blank=False,null=False,validators=[MinValueValidator(0)])
    id_sesion=models.CharField(max_length=50,default='')
