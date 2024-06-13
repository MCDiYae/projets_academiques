from . import views
from django.urls import path

urlpatterns = [
    path('1', views.index, name='index'),
    path('2', views.index2, name='index2')
]