from django.urls import path
from .views import VRegistro, cerrar_sesion, logear                                # Vista donde resuelvo la ruta

urlpatterns = [ 
    path('', VRegistro.as_view(), name="autenticacion"),
    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
    path('ingreso', logear, name='ingreso')
 ]