from django.db import models

from Client.models import Client
from Livre.models import Livre


# Create your models here.


class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    livre = models.ForeignKey(Livre, on_delete=models.SET_NULL, null=True)
    dateCreation = models.DateField(auto_now_add=True)
    qte = models.IntegerField(null=True)