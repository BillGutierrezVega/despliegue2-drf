from rest_framework import routers
from django.urls import path, include
from . import views


router = routers.DefaultRouter()
router.register(r'artista', views.ArtistaViewSet)
router.register(r'cancion', views.CancionViewSet)
router.register(r'playlist', views.PlaylistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]