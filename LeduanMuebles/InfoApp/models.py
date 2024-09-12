from django.db import models

# Create your models here.
class Information(models.Model):
    nombre=models.TextField(max_length=990)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Información"
        verbose_name_plural="Informaciones"

    def __str__(self):
        return self.nombre


