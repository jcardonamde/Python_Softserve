from django.db import models

class Propietario(models.Model):
    nombre   = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email    = models.EmailField()

    def __str__(self):
        return f"{self.nombre} ({self.email})"


class Mascota(models.Model):
    nombre       = models.CharField(max_length=100)
    especie      = models.CharField(max_length=50)
    edad         = models.PositiveIntegerField()
    propietario  = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return f"{self.nombre} — {self.especie}"