from django.db import models

# Create your models here.
class Oferta(models.Model):
    nombre=models.TextField(max_length=990)
    imagen=models.ImageField(upload_to="ofertas")
    precio=models.CharField(max_length=50)
    informacion=models.TextField(max_length=990)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Oferta"
        verbose_name_plural="Ofertas"

    def __str__(self):
        return self.nombre

