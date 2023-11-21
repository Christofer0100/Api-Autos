from django.db import models

# Create your models here.
class Alumno(models.Model):
    idAlumno = models.IntegerField(primary_key=True, verbose_name = "Id de Usuario")
    Gmail = models.CharField(max_length=50, verbose_name = "Gmail")
    Contrasena = models.CharField(max_length=50, verbose_name = "Contrasena")
    nombreAlumno = models.CharField(max_length=50, verbose_name = "Nombre de Usuario")

    def __str__(self):
        return self.nombreAlumno
    

class Conductor(models.Model):
    idConductor = models.IntegerField(primary_key=True, verbose_name = "Id de Conductor")
    Gmail = models.CharField(max_length=50, verbose_name = "Gmail")
    Contrasena = models.CharField(max_length=50, verbose_name = "Contrasena")
    nombreConductor = models.CharField(max_length=50, verbose_name = "Nombre de Conductor")

    def __str__(self):
        return self.nombreConductor