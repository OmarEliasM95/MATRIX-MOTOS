from django.contrib import admin
from .models import *

class Lista_Comprados(admin.TabularInline):
    model=Compra_intermedio
    extra=1
class ComprasAdmin(admin.ModelAdmin):
    list_display = ('fecha_compra','proveedor','total','metodo_pago')
    inlines=[Lista_Comprados]
admin.site.register(Compra, ComprasAdmin)
admin.site.register(Compra_intermedio)