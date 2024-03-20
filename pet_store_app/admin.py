from django.contrib import admin
from .models import Owner, Dog, Cat, ExoticAnimal

# Register your models here.
admin.site.register([Owner, Dog, Cat, ExoticAnimal])