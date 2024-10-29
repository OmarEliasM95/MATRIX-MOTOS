from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('panel_compras/', views.panel_compras, name='panel_compras'),
    path('seleccionar_proveedor/', views.seleccionar_proveedor, name='seleccionar_proveedor'),
    path('agregar_producto_compra/<int:id_producto>/', views.agregar_producto_compra, name='agregar_producto_compra'),
    path('eliminar_producto_compra/<int:id_producto>/', views.eliminar_producto_compra, name='eliminar_producto_compra'),
    path('confirmar_compra/', views.confirmar_compra, name='confirmar_compra'),
    path('grafico_compras',views.grafico_compras,name="grafico_compras")
]