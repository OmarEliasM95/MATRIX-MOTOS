from django.urls import path
from . import views

urlpatterns = [
    path('panel_proveedores/', views.panel_proveedores, name='panel_proveedores'),
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('editar_proveedor/<int:id_proveedor>/', views.editar_proveedor, name='editar_proveedor'),
    path('eliminar_proveedor/<int:id_proveedor>/', views.eliminar_proveedor, name='eliminar_proveedor'),
]