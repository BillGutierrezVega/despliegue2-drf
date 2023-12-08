from rest_framework import viewsets
from .serializers import CancionSerializer, PlaylistSerializer, ArtistaSerializer
from .models import Playlist, Cancion, Artista


# Create your views here.
class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
    

class CancionViewSet(viewsets.ModelViewSet):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer
    

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    