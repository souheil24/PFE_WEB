from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.connexion_view, name='connexion'),
    path('acceuil/', views.acceuil, name='home'),  # Exemple pour la page d'accueil
    
]