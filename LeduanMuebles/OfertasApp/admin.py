from django.contrib import admin
from .models import Oferta

# Register your models here.

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen', 'precio', 'informacion', 'created', 'updated')

admin.site.register(Oferta, OfertaAdmin)
