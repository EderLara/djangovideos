from email.headerregistry import ContentDispositionHeader
from ssl import create_default_context
from django.db import models

# Create your models here.

# Funcion para cargar imágenes den servicios:
def upload_imagen_servicios(instance, filename):
    return 'servicios/' + filename


class Servicios(models.Model):
    titulo = models.CharField(max_length = 50)
    contenido = models.CharField(max_length = 50)
    imagen = models.ImageField(upload_to = upload_imagen_servicios)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self) -> str:
        return self.titulo
