from django.db import models
from Proveedores.models import Proveedor
from django.core.validators import MinValueValidator

class Producto(models.Model):
    nombre=models.CharField(max_length=100, blank=False, null=False)
    precio=models.DecimalField(max_digits=10, decimal_places=2,blank=False, null=False,validators=[MinValueValidator(0)]) 
    existencias=models.PositiveIntegerField(default=0, blank=False,null=False)
    stock_maximo=models.PositiveIntegerField(default=0, blank=True,null=True,validators=[MinValueValidator(0)])
    stock_minimo=models.PositiveIntegerField(default=0, blank=True,null=True,validators=[MinValueValidator(0)])
    proveedores=models.ManyToManyField(Proveedor, through='Producto_Intermedia')
    def __str__(self):
        return f"{self.nombre}"
    
class Producto_Intermedia(models.Model):
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    