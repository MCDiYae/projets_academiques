from datetime import datetime

from django.db import models

# Create your models here.


class Livre(models.Model):
    CATEGORY = (
        ('Physique', 'Physique'),
        ('Mathématique', 'Mathématique'),
        ('Chimie', 'Chimie'),
        ('Science', 'Science'),
        ('Enfant', 'Enfant'),
        ('Informatique', 'Informatique')
    )
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image_covr = models.ImageField(upload_to='photos/%y/%m/%d', null=True)
    quantite = models.IntegerField()
    pages = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=190, null=True, choices=CATEGORY)
    date_edition = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.titre
