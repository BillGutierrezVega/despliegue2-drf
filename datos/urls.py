from django.urls import path

from . import views

urlpatterns = [
    path('', views.datos, name='datos'),
    path('envia/', views.envia, name='envia'),
    path('envia_cancion/', views.envia_cancion, name='envia_cancion'),
]