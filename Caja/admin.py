from django.contrib import admin
from .models import *

class CajaAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'fecha_apertura', 'saldo_inicial', 'fecha_cierre', 'saldo_final')

class DineroAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'fecha_dinero', 'ing_egre', 'tipo_dinero')

admin.site.register(Caja, CajaAdmin)
admin.site.register(Dinero, DineroAdmin)