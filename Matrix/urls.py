from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler400, handler403 ,handler404,handler500
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Empleados.urls')),
    path('menu/',views.menu, name="menu"),
    path('', include('Caja.urls')),
    path('',include('Ventas.urls')),
    path('', include('Compras.urls')),
    path('', include('Proveedores.urls')),
    path('', include('Productos.urls')),
    path('', include('Gastos.urls')),
    path('panel_historial/',views.panel_historial, name="panel_historial"),
    path('historial_compras/', views.historial_compras,name='historial_compras'),
    path('ver_detalle_compra/<int:id_compras>/',views.ver_detalle_compra, name='ver_detalle_compra'),
    path('historial_ventas/', views.historial_ventas,name='historial_ventas'),
    path('ver_detalle_ventas/<int:id_ventas>/',views.ver_detalle_venta, name='ver_detalle_venta')    
]
if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler400 = 'Matrix.views.error_400'  
handler403 = 'Matrix.views.error_403'  
handler404 = 'Matrix.views.error_404'  
handler500 = 'Matrix.views.error_500'  