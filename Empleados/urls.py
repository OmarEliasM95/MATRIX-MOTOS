from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_empleado, name='login'),
    path('cerrar_sesion/', views.logout_empleado, name='cerrar_sesion'),
    path('panel_empleado/', views.panel_empleado, name='panel_empleado'),
    path('agregar_empleado/', views.agregar_empleado, name='agregar_empleado'),
    path('editar_empleado/<int:id_empleado>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar_empleado/<int:id_empleado>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('cambiar_contraseña/<int:id_empleado>/', views.cambiar_contraseña, name='cambiar_contraseña'),
    path('panel_perfil', views.panel_perfil,name='panel_perfil'),  
]
