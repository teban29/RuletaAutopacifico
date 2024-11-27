from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    numero_documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    numero_celular = models.CharField(max_length=11)
    numero_factura = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Premio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    probabilidad = models.FloatField()
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Ruleta(models.Model):
    premio = models.ForeignKey(Premio, on_delete=models.CASCADE, null=True, blank=True)
    fecha_tiro = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Tiro lanzado por {self.cliente.nombre} el {self.fecha_tiro}"
    
    
    
class Ganador(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    premio = models.ForeignKey(Premio, on_delete=models.CASCADE)
    fecha_ganador = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.cliente.nombre} ganó el premio {self.premio.nombre} el {self.fecha_ganador}"
    
class Configuracion(models.Model):
    probabilidad_no_ganar = models.FloatField(default=30)  # Valor por defecto del 30%

    def __str__(self):
        return f"Probabilidad de no ganar: {self.probabilidad_no_ganar}%"
