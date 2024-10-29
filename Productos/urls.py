from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('lista_producto/', views.lista_producto , name='lista_producto'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:id_producto>/', views.editar_producto, name='editar_producto')
]