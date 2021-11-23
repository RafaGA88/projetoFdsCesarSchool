from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'principal'),
    path('listagem/', views.listagem, name = 'listagem'),
    path('anime/<int:anime_id>', views.anime, name = 'anime'),
    path('cadastrar_anime/', views.cadastrarAnime, name = 'cadastrarAnime'),
    path('cadastrar_episodio/', views.cadastrarEpisodio, name = 'cadastrarEpisodio'),
    path('episodio/<int:episodio_id>', views.episodio, name = 'episodio')
] 