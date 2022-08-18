from django.urls import path
from Servicios import views                     # Vista donde resuelvo la ruta

urlpatterns = [ 
    path('', views.servicios, name="servicios"),
 ]