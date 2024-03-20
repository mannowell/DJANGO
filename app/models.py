from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    animal = models.TextField(max_length=255)
    especie = models.TextField(max_length=255)
