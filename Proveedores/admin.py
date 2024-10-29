from django.contrib import admin
from .models import *

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'telefono', 'email', 'dirección', 'provincia')

admin.site.register(Proveedor, ProveedoresAdmin)
