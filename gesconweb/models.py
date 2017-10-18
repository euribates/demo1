from django.db import models

# Create your models here.

class Aplicativo(models.Model):

    nombre = models.CharField(max_length=82)
    url = models.URLField(max_length=400)
    f_creacion = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=300, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return '{} (Creada el {})'.format(self.nombre, self.f_creacion)
