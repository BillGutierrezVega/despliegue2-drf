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
    nuevo_artista = {'nombre':'cn59', 'genero':'alternaativo'}
    response = requests.post(ruta, json=nuevo_artista)
    data = response.json()
    return render(request, template, {'data':data})

def envia_cancion(request):
    nueva_cancion = {
        'titulo':'una cancion de perdon',
        'artista':1,
        'letras':'letras de la cancion'
    }
    response = requests.post('https://bill-despliegue-drf.onrender.com/cancion/', json=nueva_cancion)
    data = response.json
    return render(request, template, {'data':data})
