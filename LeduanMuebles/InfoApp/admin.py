from django.contrib import admin
from .models import Information

# Register your models here.
class InformationAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')

admin.site.register(Information, InformationAdmin)

