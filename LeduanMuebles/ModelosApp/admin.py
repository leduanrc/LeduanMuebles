from django.contrib import admin
from .models import Mueble

# Register your models here.

class MuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen', 'precio', 'modelo', 'created', 'updated')

admin.site.register(Mueble, MuebleAdmin)
