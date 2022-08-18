from django.shortcuts import render, HttpResponse
from .models import Producto

# Create your views here.

def tienda(request):
    template = 'tienda/tienda.html'
    productos = Producto.objects.all()

    return render(request, template, {'productos':productos})

def carrito(request):
    template = 'carro/widget.html'
    return render(request, template)