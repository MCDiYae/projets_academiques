from . import views
from django.urls import path
from django.urls import re_path

urlpatterns = [
    path('', views.liste_livre, name='livre'),
    path('ajouter_livre',views.ajouter_livre,name='ajouter_livre'),
    path('detail_livre/<int:id>', views.detail_livre, name='detail_livre'),
    path('modifier_livre/<int:id>', views.modifier_livre, name='modifier_livre'),
    path('supprimer_livre/<int:id>', views.supprimer_livre, name='supprimer_livre'),

]