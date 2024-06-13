from django.db import models
from django.contrib import admin
# Create your models here.


class Student(models.Model):
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    datenaissance = models.DateField()
    CNE = models.IntegerField()
    section = models.CharField(max_length=25)


class StudentAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "datenaissance", "CNE", "section")
    list_filter = ("nom", "prenom", "datenaissance", "CNE", "section")
