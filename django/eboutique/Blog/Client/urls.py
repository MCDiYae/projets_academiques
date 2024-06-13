from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list_clients'),
    path('ajouter_client/', views.ajouter_client, name='ajouter_client'),
    path('modifier_client/<int:pk>/', views.modifier_client, name='modifier_client'),
    path('supprimer_client/<int:pk>/', views.supprimer_client, name='supprimer_client'),
    path('detail_client/<int:pk>/', views.detail_client, name='detail_client'),
]
