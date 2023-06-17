from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.IntegerField(blank=True, unique=True, null=True)
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.CharField(max_length=150, null=False)
    telefono = models.IntegerField(null=False, blank=False)

class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    raza = models.CharField(max_length=150, blank=False, null=False)
    sexo = models.CharField(max_length=1, blank=False, null=False)
    pesokg = models.FloatField(blank=False, null=True)

# Citas? Pedidos? Reservas?
class Citas(models.Model):
    id = models.AutoField(primary_key=True)

class Personal(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.IntegerField(blank=True, unique=True, null=True)
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    hora_entrada = models.TimeField(null=False, blank=False)
    hora_salida = models.TimeField(null=False, blank=False)

