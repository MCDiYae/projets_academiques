from django.db import models


class Etudiant(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    datenaisance = models.DateField(null=True)
    CNE = models.IntegerField()
    section = models.CharField(max_length=40)
    def __str__(self):
        return self.nom
