from django.contrib import admin
from .models import Etudiant

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ("CNE","nom","prenom")

admin.site.register(Etudiant, EtudiantAdmin)
# Register your models here.
