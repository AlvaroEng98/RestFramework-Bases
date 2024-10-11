from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Edificacion(models.Model):

    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descipcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900, null=False, blank=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='edificacion_list')

    def __str__(self) -> str:
        return self.direccion
    

class Comentario(models.Model):

    calificacion = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    edificacion = models.ForeignKey(Edificacion, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self) -> str:
        return str(self.calificacion) + " " + self.edificacion.direccion