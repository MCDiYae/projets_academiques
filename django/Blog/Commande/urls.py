from . import views
from django.urls import path

urlpatterns = [
    path('', views.list_commande, name='commande'),
    path('supprimer_commande/<int:id>/', views.supprimer_commande, name='supprimer_commande'),
]