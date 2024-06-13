from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ajouter_livre/', views.ajouter_livre, name='ajouter_livre'),
    path('modifier_livre/<int:pk>/', views.modifier_livre, name='modifier_livre'),
    path('supprimer_livre/<int:pk>/', views.supprimer_livre, name='supprimer_livre'),
    #path('detail_livre/<int:pk>/', views.detail_livre, name='detail_livre'),
    re_path(r"^article/(?P<pk>[\w-]+)/$", views.detail_livre, name="detail_livre"),
]
