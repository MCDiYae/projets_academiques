from django.forms import ModelForm, DateTimeInput
from .models import Livre

class LivreForm(ModelForm):
    class Meta:
        model=Livre
        fields='__all__'
            # {'titre','auteur','prix','discription','image_covr','quantite','pages','category','date_edition'}
        widgets = {
            'date_edition': DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }