from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from rendez_vous_web.forms import FormulaireDeConnexionUtilisateur, FormulaireDeCreationUtilisateur
from rendez_vous_web.models import Utilisateur, Rendez_vous, Message

def accueil(request):
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    return render(request, 'accueil.html')

def connexion(request):
    if request.method == 'POST':
        form = FormulaireDeConnexionUtilisateur(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['mot_de_passe']

            user = authenticate(username=email, password=mot_de_passe)

            if user is not None:
                login(request, user)
                return redirect('accueil')
            else:
                return redirect('connexion')
    else:
        form = FormulaireDeConnexionUtilisateur()
    return render(request, 'connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('accueil')

def inscription(request):
    if request.method == 'POST':
        form = FormulaireDeCreationUtilisateur(request.POST)

        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            mot_de_passe = form.cleaned_data['mot_de_passe']
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['telephone']
            role = form.cleaned_data['role']

            user = User.objects.create_user(email , email, mot_de_passe)
            user.last_name = nom
            user.first_name = prenom
            user.save()
            user = User.objects.get(email=email)
            utilisateur = Utilisateur(user=user, telephone=telephone, role=role)
            utilisateur.save()
            return redirect('connexion')
    else:
        form = FormulaireDeCreationUtilisateur()
    return render(request, 'inscription.html', {'form': form})

def liste_des_enseignants(request):
    enseignants = User.objects.filter(utilisateur__role='Enseignant')
    return render(request, 'liste-des-enseignants.html', {"enseignants": enseignants})