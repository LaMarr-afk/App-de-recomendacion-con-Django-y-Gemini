from django.db import models


class Comentario(models.Model):
    comentarios=models.CharField(max_length=200)
    respuesta=models.CharField(max_length=200)