from django.contrib import admin
from .models import *

class Lista_Vendidos(admin.TabularInline):
    model=Productos_Vendidos
    extra=1
class VentaAdmin(admin.ModelAdmin):
    list_display = ('fecha','total_venta','metodo_pago')
    inlines=[Lista_Vendidos]

admin.site.register(Venta, VentaAdmin)
admin.site.register(Productos_Vendidos)