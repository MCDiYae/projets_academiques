from django.db import models


# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=30, null=True)
    prenom = models.CharField(max_length=30, null=True)
    email=models.EmailField()
    tel=models.CharField(max_length=16)
    dateCreation=models.DateField(auto_now_add=True)