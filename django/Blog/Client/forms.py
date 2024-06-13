from django.forms import ModelForm, DateTimeInput
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model=Client
        fields='__all__'
        widgets = {
            'date_edition': DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }