from django.contrib import admin
from .models import Categoria, Post

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'contenido']
    list_display = ['titulo','contenido','autor','created','updated']
    list_filter = ['titulo','autor','created']
    readonly_fields = ('created', 'updated')

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Post, PostAdmin)
