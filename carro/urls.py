from django.urls import path
from . import views                     # Vista donde resuelvo la ruta

app_name = 'carro'      # Con esta variable nos aseguramos que el nombre de las rutas se conservan en esta aplicacion
                        # por si existe otra aplicacion con los mismos nombres de las rutas

urlpatterns = [ 
    path('agregar/<int:producto_id>/', views.agregar_producto, name="agregar"),
    path('adicionar/<int:producto_id>/', views.adicionar_producto, name="adicionar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carro, name="limpiar"),
 ]