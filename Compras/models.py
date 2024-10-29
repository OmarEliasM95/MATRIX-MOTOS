from django.db import models
from Productos.models import Producto
from Proveedores.models import Proveedor
from datetime import datetime
from Caja.models import Caja  
from Empleados.models import Empleado

Metodos_Pagos = [('', ''), ('Efectivo', 'Efectivo'), ('Transferencia', 'Transferencia'),
                 ('Tarjeta_de_Debito', 'Tarjeta de Debito')]

class Compra(models.Model):
    fecha_compra = models.DateTimeField(default=datetime.now)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, blank=True, null=True)
    productos = models.ManyToManyField(Producto, through='compra_intermedio')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=25, choices=Metodos_Pagos, default='', blank=True)
    id_sesion = models.CharField(max_length=20, default='')
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE, related_name='compras', null=True)

    def __str__(self):
        return f"Compra de {self.total} - {self.metodo_pago} ({self.fecha_compra})"


class Compra_intermedio(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_de_compra = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0, max_digits=10, decimal_places=2)