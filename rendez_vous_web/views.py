from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from rendez_vous_web.forms import FormulaireDeConnexionUtilisateur
from rendez_vous_web.forms import FormulaireDeCreationUtilisateur
from rendez_vous_web.models import Utilisateur

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

            user = User.objects.get(email=email)
            validation_du_mot_de_passe = check_password(mot_de_passe, user.password)

            if validation_du_mot_de_passe:
                utilisateur = {
                    'id': user.id,
                    'nom': user.last_name,
                    'prénom': user.first_name,
                    'mot_de_passe': user.password,
                    'role': user.utilisateur.role,
                    'téléphone': user.utilisateur.telephone,
                    'email': user.email,
                    'date_ajout': str(user.date_joined)
                }
                request.session['utilisateur'] = utilisateur
                return redirect('accueil')
            else:
                return redirect('connexion')
    else:
        form = FormulaireDeConnexionUtilisateur()
    return render(request, 'connexion.html', {'form': form})

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