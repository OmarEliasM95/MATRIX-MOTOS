from django.urls import path
from . import views

urlpatterns = [
    path('panel_venta/', views.panel_venta, name='panel_venta'),
    path('agregar_producto/<int:id_producto>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto_vendido/<int:id_producto>/', views.eliminar_producto_vendido, name='eliminar_producto_vendido'),
    path('crear_factura/<int:id_venta>/', views.crear_factura, name='crear_factura'),
    path('nueva_venta', views.nueva_venta, name='nueva_venta'),
    path('grafico_ventas/',views.grafico_ventas,name='grafico_ventas')
]