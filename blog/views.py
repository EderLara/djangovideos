from django.shortcuts import render, HttpResponse
from .models import Categoria, Post

# Create your views here.

def blog(request):
    publicaciones = Post.objects.all()      # Consulta a la tabla
    template_name = 'blog/blog.html'        # Nombre de la plantilla
    categorias = Categoria.objects.all()    # Consulta a tabla categorías
    return render(request, template_name, {'publicaciones': publicaciones, 'categorias': categorias})

def categoria(request, categoria_id):
    template_name = 'blog/categorias.html'                      # Nombre de la plantilla
    categoria = Categoria.objects.get(id = categoria_id)        # Consulta a tabla categorías con filtro
    publicaciones = Post.objects.filter(categorias = categoria)
    categorias = Categoria.objects.all()                        # Consulta a tabla categorías
    return render(request, template_name, {'categoria': categoria, 'publicaciones': publicaciones, 'categorias': categorias})
