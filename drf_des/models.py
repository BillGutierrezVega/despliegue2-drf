from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=150)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    titulo = models.CharField(max_length=150)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    letras = models.TextField()
    
    def __str__(self):
        return self.titulo


class Playlist(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    canciones = models.ManyToManyField(Cancion)
    
    def __str__(self):
        return self.nombre