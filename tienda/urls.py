from django.urls import path
from tienda import views                     # Vista donde resuelvo la ruta

urlpatterns = [ 
    path('', views.tienda, name="tienda"),
    path('carro/', views.carrito, name="carrito")
 ]