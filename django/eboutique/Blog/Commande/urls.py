from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list_commandes'),
    path('ajouter_commande/', views.ajouter_commande, name='ajouter_commande'),
    path('modifier_commande/<int:pk>/', views.modifier_commande, name='modifier_commande'),
    path('supprimer_commande/<int:pk>/', views.supprimer_commande, name='supprimer_commande'),
]
