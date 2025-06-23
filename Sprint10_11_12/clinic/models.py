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
    

class Cita(models.Model):
    mascota     = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='citas')
    fecha       = models.DateTimeField()
    motivo      = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.mascota.nombre} @ {self.fecha:%Y-%m-%d %H:%M} - {self.motivo}"


class Medicamento(models.Model):
    nombre       = models.CharField(max_length=100)
    descripcion  = models.TextField(blank=True)
    cantidad     = models.PositiveIntegerField(default=0)
    fecha_venc   = models.DateField()
    def __str__(self): return self.nombre


class Cirugia(models.Model):
    mascota      = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='cirugias')
    veterinario  = models.CharField(max_length=100)
    fecha_plan   = models.DateTimeField()
    descripcion  = models.TextField()
    def __str__(self): 
        return f"{self.mascota.nombre} @ {self.fecha_plan:%Y-%m-%d}"
   

class Bitacora(models.Model):
    cita     = models.ForeignKey(Cita, on_delete=models.CASCADE, related_name='bitacoras')
    observacion  = models.TextField()
    tratamiento  = models.TextField(blank=True)
    creada_en    = models.DateTimeField(auto_now_add=True)
    def __str__(self): 
        return f"Bitácora {self.id} – {self.consulta.mascota.nombre} @ {self.creada_en:%Y-%m-%d %H:%M}"
