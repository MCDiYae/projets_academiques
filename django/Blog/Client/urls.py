from . import views
from django.urls import path

urlpatterns = [
    path('list_client', views.list_client, name='list_client'),
    path('ajouter_client', views.ajouter_client, name='ajouter_client'),
]