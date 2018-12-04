from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class Usuario(admin.ModelAdmin):
    model= Usuario
    list_display = ['user','document']
