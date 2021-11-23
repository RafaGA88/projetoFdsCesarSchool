from enum import auto
from django.db import models

class Usuario(models.Model):
    
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    #models.TextField = texto
    #models.DateTimeField = data
    #models.IntegerField = inteiro

    #blank = true - opcional

    



