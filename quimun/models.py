from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(max_length=10)
    name = models.TextField()

class Empresa(models.Model):
    name = models.TextField()

class Arriendo(models.Model):
    id_cliente = models.IntegerField()
    id_empresa = models.IntegerField()
    costo_diario = models.IntegerField()
    dias = models.IntegerField()
