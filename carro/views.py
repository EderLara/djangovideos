from django.shortcuts import render, redirect

# importamos la clase Carro:
from .carro import Carro
# Importamos el modelo de datos de productos:
from tienda.models import Producto

# Create your views here.
def agregar_producto(request, producto_id):
    # Creamos la instancia de carro:
    carro = Carro(request)                                  # Creamos el objeto carro de la Clase Carro
    # Capturamos el id del modelo de productos:
    producto = Producto.objects.get(id = producto_id)       # Obtenemos el producto y lo adicionamos al carro
    # Ejecutamos la funcion agregar:
    carro.agregar(producto=producto)                        # Agregamos el producto al carro
    # Redireccionamos a la tienda:
    return redirect("tienda")                               # Nos redirigimos al catalogo de la tienda

def adicionar_producto(request, producto_id):
    # Creamos la instancia de carro:
    carro = Carro(request)                                  # Creamos el objeto carro de la Clase Carro
    # Capturamos el id del modelo de productos:
    producto = Producto.objects.get(id = producto_id)       # Obtenemos el producto y lo adicionamos al carro
    # Ejecutamos la funcion agregar:
    carro.agregar(producto=producto)                        # Agregamos el producto al carro
    # Redireccionamos a la tienda:
    return redirect("carrito")                              # Nos redirigimos al catalogo de la tienda


def eliminar_producto(request, producto_id):
    # Creamos la instancia de carro:
    carro = Carro(request)                                  # Creamos el objeto carro de la Clase Carro
    # Capturamos el id del modelo de productos:
    producto = Producto.objects.get(id = producto_id)       # Obtenemos el producto y lo adicionamos al carro
    # Ejecutamos la funcion eliminar:
    carro.eliminar(producto=producto)                       # Eliminamos el producto del carro
    # Redireccionamos a la tienda:
    return redirect("carrito")                               # Nos redirigimos al catalogo de la tienda

def restar_producto(request, producto_id):
    # Creamos la instancia de carro:
    carro = Carro(request)                                  # Creamos el objeto carro de la Clase Carro
    # Capturamos el id del modelo de productos:
    producto = Producto.objects.get(id = producto_id)       # Obtenemos el producto y lo adicionamos al carro
    # Ejecutamos la funcion restar:
    carro.restar_producto(producto=producto)                # Eliminamos una unidad del producto del carro
    # Redireccionamos a la tienda:
    return redirect("carrito")                               # Nos redirigimos al catalogo de la tienda

def limpiar_carro(request, producto_id):
    # Creamos la instancia de carro:
    carro = Carro(request)                                  # Creamos el objeto carro de la Clase Carro
    # Ejecutamos la funcion agregar:
    carro.limpiar_carro()                                   # Eliminamos una unidad del producto del carro
    # Redireccionamos a la tienda:
    return redirect("tienda")                               # Nos redirigimos al catalogo de la tienda