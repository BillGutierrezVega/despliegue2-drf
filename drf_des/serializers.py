from rest_framework import serializers
from .models import Cancion, Playlist, Artista

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'


class CancionSerializer(serializers.ModelSerializer):
    artista = ArtistaSerializer(read_only=True)
    class Meta:
        model = Cancion
        fields = '__all__'
        

class PlaylistSerializer(serializers.ModelSerializer):
    canciones = CancionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Playlist
        fields = '__all__'