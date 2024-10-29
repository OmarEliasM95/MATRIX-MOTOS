from django.urls import path
from . import views

urlpatterns = [
    path('apertura/', views.apertura_view , name='apertura' ),
    path('cierre/', views.cierre_view, name='cierre'),
    path('panel_dinero/',views.panel_dinero, name='panel_dinero'),
    path('agregar_dinero/', views.agregar_dinero, name='agregar_dinero'),
    path('datos_caja/',views.datos_caja,name="datos_caja")
]
