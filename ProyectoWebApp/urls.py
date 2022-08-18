from django.urls import path
from ProyectoWebApp import views                                # Vista donde resuelvo la ruta

urlpatterns = [ 
    path('', views.home, name="home"),
 ]