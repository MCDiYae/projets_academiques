from django.db import models
from django.contrib import admin
# Create your models here.


class Client(models.Model):
    nom = models.CharField(max_length=30, null=True)
    prenom = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=26)
    dateCreation = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email


class ClientAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "email", "telephone", "dateCreation")
    list_filter = ("nom",)

