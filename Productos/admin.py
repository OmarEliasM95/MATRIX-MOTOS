from django.contrib import admin
from .models import *

class Lista_Proveedores(admin.TabularInline):
    model=Producto_Intermedia
    extra=1
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'existencias')
    inlines=[Lista_Proveedores]


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Producto_Intermedia)

