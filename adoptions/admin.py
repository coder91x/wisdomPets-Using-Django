from django.contrib import admin
from .models import Pet
@admin.register(Pet)
class Pet_admin(admin.ModelAdmin):
    list_display = ['name', 'age', 'color']

