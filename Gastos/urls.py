from django.urls import path
from . import views

urlpatterns = [
    path('gasto_panel/',views.gasto_panel, name='gasto_panel'),
    path('agregar_gasto/', views.agregar_gasto, name='agregar_gasto')
]