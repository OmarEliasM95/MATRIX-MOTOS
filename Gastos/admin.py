from django.contrib import admin
from .models import *
class GastoAdmin(admin.ModelAdmin):
    list_display=('fecha','descripcion_gasto','costo')
admin.site.register(Gasto,GastoAdmin)
