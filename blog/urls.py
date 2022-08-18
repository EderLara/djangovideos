from django.urls import path
from blog import views                     # Vista donde resuelvo la ruta
from django.urls.resolvers import URLPattern            # Resuelve las Rutas

urlpatterns = [ 
    path('', views.blog, name="blog"),
    path('categoria/<int:categoria_id>', views.categoria, name="categoria"),
 ]