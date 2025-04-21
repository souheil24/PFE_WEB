from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

def connexion_view(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')

        # Vérifier si l'identifiant est un email ou un username
        user = None
        if '@' in identifier:
            try:
                user_obj = User.objects.get(email=identifier)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
        else:
            user = authenticate(request, username=identifier, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirigez vers la page d'accueil ou une autre page
        else:
            messages.error(request, "Identifiants invalides. Veuillez réessayer.")

    return render(request, 'Plateforme/connexion.html')

def acceuil(request):
    return render(request, 'Plateforme/acceuil.html')

