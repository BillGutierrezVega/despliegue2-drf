from django.shortcuts import render
import requests
from django.http import HttpResponse

ruta = 'https://bill-despliegue-drf.onrender.com/artista/'
template = 'datos.html'
# Create your views here.
def datos(request):
    response = requests.get(ruta)
    data = response.json
    return render(request, template, {'data':data})

def envia(request):
    nuevo_artista = {'nombre':'jenny', 'genero':'regge'}
    response = requests.post(ruta, json=nuevo_artista)
    data = response.json()
    return render(request, template, {'data':data})

def envia_cancion(request):
    nueva_cancion = {
        'titulo':'cancion de amo',
        'artista':3,
        'letras':'hace mucho no sentia lo que siento en este dia'
    }
    response = requests.post('https://bill-despliegue-drf.onrender.com/cancion/', json=nueva_cancion)
    data = response.json
    return render(request, template, {'data':data})

def envia_playlist(request):
    nueva_playlist = {
        'nombre': 'Mi Lista de Reproducción favorita',
        'descripcion': 'Descripción de la lista de reproducción 2',
        'canciones': [1, 2, 3]  # IDs de las canciones que pertenecen a la lista de reproducción
    }

    response = requests.post('https://bill-despliegue-drf.onrender.com/playlist/', json=nueva_playlist)
    data = response.json()

    return render(request, template, {'data': data})

import requests

def traer_playlist(request):
    response = requests.get('https://bill-despliegue-drf.onrender.com/playlist/')
    playlists = response.json()

    # Obtener detalles de cada canción en cada lista de reproducción
    for playlist in playlists:
        playlist['canciones_detalles'] = []
        for cancion_id in playlist['canciones']:
            cancion_details = obtener_detalles_cancion(cancion_id)
            playlist['canciones_detalles'].append(cancion_details)
        
        del playlist['canciones']
    
    nombre = playlists[1]['canciones_detalles'][2]['titulo']
    
    return render(request, template, {'playlists': playlists, 'nombre':nombre})

def obtener_detalles_cancion(cancion_id):
    response = requests.get(f'https://bill-despliegue-drf.onrender.com/cancion/{cancion_id}/')
    cancion_details = response.json()
    return cancion_details
