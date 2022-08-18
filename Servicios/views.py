from django.shortcuts import render
from .models import Servicios        # <- Importamos el modelo de servicios

# Create your views here.

def servicios(request):
    # variable de objetos de la tabla servicios:
    servicios = Servicios.objects.all()
    # agregamos a la funcion render, un diccionario con todos los servicios encontrados:
    return render(request, 'servicios/servicios.html', {'servicios': servicios});
    