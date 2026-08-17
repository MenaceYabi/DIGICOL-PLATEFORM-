from django.urls import path 
from .import views

urlpatterns = [
    path('', views.Accueil , name="Acceuil")
]