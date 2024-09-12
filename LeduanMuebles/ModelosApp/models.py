from django.db import models

# Create your models here.

class Mueble(models.Model):
    nombre=models.TextField(max_length=990)
    imagen=models.ImageField(upload_to="muebles")
    precio=models.CharField(max_length=50)
    modelo=models.CharField(max_length=990)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Mueble"
        verbose_name_plural="Muebles"

    def __str__(self):
        return self.nombre
