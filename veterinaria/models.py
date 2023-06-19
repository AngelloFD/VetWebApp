from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.IntegerField(blank=True, unique=True, null=True)
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.CharField(max_length=150, null=False)
    telefono = models.IntegerField(null=False, blank=False)
    def __str__(self):
        return self.nombres + ' ' + self.apellidos
    

class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    raza = models.CharField(max_length=150, blank=False, null=False)
    sexo = models.CharField(max_length=1, blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    pesokg = models.FloatField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + ' ' + self.cliente.apellidos

class Personal(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.IntegerField(blank=True, unique=True, null=True)
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=100, null=True, blank=True)
    estado = models.BooleanField(default=False)
    def __str__(self):
        return self.nombres + ' ' + self.apellidos

class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    razon = models.CharField(max_length=150, null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    hora = models.TimeField(null=False, blank=False)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    def __str__(self):
        return self.personal.nombres + ' ' + self.cliente.apellidos + ' ' + self.mascota.nombre



