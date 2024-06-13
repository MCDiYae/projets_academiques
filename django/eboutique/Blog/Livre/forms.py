
from django.forms import ModelForm, DateTimeInput

from .models import Livre


class LivreForm(ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'prix', 'description', 'image_covr', 'quantite', 'pages', 'category',
                  'date_edition']
        widgets = {
            'date_edition': DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

