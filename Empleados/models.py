from django.contrib.auth.models import AbstractUser
from django.db import models

class Empleado(AbstractUser):
    dni=models.IntegerField(null=True, blank=True, verbose_name="DNI")
    dirección=models.CharField(null=True, blank=True, max_length=150)
    telefono=models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.username