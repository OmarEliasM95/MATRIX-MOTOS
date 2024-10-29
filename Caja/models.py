from django.db import models
from Empleados.models import Empleado
from datetime import datetime
from django.core.validators import MinValueValidator 

Tipo_Dinero=[('',''),('Ingreso','Ingresar'),('Egreso','Retirar')]
estado_caja=[('Abierta','Abierta'),('Cerrada','Cerrada')]
class Caja(models.Model):
    empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE,null=True,blank=True)
    fecha_apertura=models.DateTimeField(default=datetime.now)
    saldo_inicial=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0)])
    fecha_cierre=models.DateTimeField(null=True,blank=True)
    saldo_final=models.IntegerField(null=True, blank=True)  
    estado= models.CharField(max_length=10,choices=estado_caja, default='Abierta')      
    def __str__(self):
        return f"{self.empleado} {self.fecha_apertura} {self.fecha_cierre} {self.saldo_final} - {self.estado}"
class Dinero(models.Model):
    empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE,null=True,blank=True)
    fecha_dinero=models.DateTimeField(default=datetime.now)
    ing_egre=models.IntegerField(verbose_name='Ingreso/Egreso')
    tipo_dinero=models.CharField(max_length=25, choices=Tipo_Dinero,default='')
    id_sesion=models.CharField(max_length=50,default='')