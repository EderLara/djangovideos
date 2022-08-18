from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre',)
    list_filter = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre','categorias','precio','disponibilidad')
    list_filter = ('nombre','categorias')
    list_per_page = 25

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)