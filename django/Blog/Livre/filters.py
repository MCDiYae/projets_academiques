import django_filters
from .models import Livre

class LivreFilter(django_filters.FilterSet):
    class Meta:
        model=Livre
        fields='__all__'
        exclude=['image_covr']