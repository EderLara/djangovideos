from django.urls import path
from . import views                     # Vista donde resuelvo la ruta

urlpatterns = [ 
    path('', views.contacto, name="contacto"),
 ]