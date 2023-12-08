from django.contrib import admin
from .models import Cancion, Artista, Playlist

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero', )
    search_fields = ('nombre', )

# Register your models here.
admin.site.register(Cancion)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Playlist)