from django.contrib import admin

from .models import Pet,Vaccine

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
