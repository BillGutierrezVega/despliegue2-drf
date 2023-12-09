from django.urls import path

from . import views

urlpatterns = [
    path('', views.datos, name='datos'),
    path('envia/', views.envia, name='envia'),
    path('envia_cancion/', views.envia_cancion, name='envia_cancion'),
    path('envia_playlist/', views.envia_playlist, name='envia_playlist'),
    path('traer_playlist/', views.traer_playlist, name='traer_playlist'),
]