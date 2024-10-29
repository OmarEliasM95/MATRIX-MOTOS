from django.db import models

class Proveedor(models.Model):
    PROVINCIAS = [
    ('Buenos Aires', 'Buenos Aires'),
    ('Catamarca', 'Catamarca'),
    ('Chaco', 'Chaco'),
    ('Chubut', 'Chubut'),
    ('Córdoba', 'Córdoba'),
    ('Corrientes', 'Corrientes'),
    ('Entre Ríos', 'Entre Ríos'),
    ('Formosa', 'Formosa'),
    ('Jujuy', 'Jujuy'),
    ('La Pampa', 'La Pampa'),
    ('La Rioja', 'La Rioja'),
    ('Mendoza', 'Mendoza'),
    ('Misiones', 'Misiones'),
    ('Neuquén', 'Neuquén'),
    ('Río Negro', 'Río Negro'),
    ('Salta', 'Salta'),
    ('San Juan', 'San Juan'),
    ('San Luis', 'San Luis'),
    ('Santa Cruz', 'Santa Cruz'),
    ('Santa Fe', 'Santa Fe'),
    ('Santiago del Estero', 'Santiago del Estero'),
    ('Tierra del Fuego', 'Tierra del Fuego'),
    ('Tucumán', 'Tucumán'),
]
    nombre=models.CharField(max_length=100,blank=False,null=False)
    telefono=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=100, blank=False,null=False)
    dirección=models.CharField(max_length=100)
    provincia=models.CharField(max_length=100,choices=PROVINCIAS,blank=False,null=False)
    def __str__(self):
        return f"{self.nombre}"
