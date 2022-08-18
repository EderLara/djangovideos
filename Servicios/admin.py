from django.contrib import admin
from .models import Servicios

# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo','contenido')
    list_filter = ('titulo','contenido')
    list_per_page = 3

admin.site.register(Servicios, ServiciosAdmin)