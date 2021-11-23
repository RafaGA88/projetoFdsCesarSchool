from typing import List
from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey

class Anime(models.Model):

    def __str__(self):
        return self.titulo

    titulo = models.CharField(max_length = 255)
    data_lancamento = models.DateTimeField()
    descricao = models.TextField()
    categoria = models.CharField(max_length= 50)

class Comentario(models.Model):
    review = models.TextField()
    rate = IntegerField()
    anime = models.ForeignKey(Anime, on_delete=DO_NOTHING)

class Episodio(models.Model):

    def __str__(self):
        return self.nome

    nome = models.CharField(max_length= 255)
    fillerOuCanon = models.BooleanField()
    numeroEpisodio = models.IntegerField()
    video = models.FileField(upload_to="video/%y", blank=True)
    animeEpisodio = models.ForeignKey(Anime, on_delete=DO_NOTHING)
