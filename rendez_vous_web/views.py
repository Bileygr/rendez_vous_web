from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from rendez_vous_web.forms import FormulaireDeConnexionUtilisateur, FormulaireDeCreationUtilisateur, FormulaireDePriseDeRendezVous, FormulaireObtentionDesID
from rendez_vous_web.models import Utilisateur, Rendez_vous, Message

def accueil(request):
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
    return render(request, 'connexion.html', {'form': FormulaireDeConnexionUtilisateur})

def deconnexion(request):
    logout(request)
    return redirect('accueil')

def inscription(request):
    if request.method == 'POST':
        form = FormulaireDeCreationUtilisateur(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['email'], form.cleaned_data['mot_de_passe'])
            user.last_name = form.cleaned_data['nom']
            user.first_name = form.cleaned_data['prenom']
            user.save()
            user = User.objects.get(email=form.cleaned_data['email'])
            utilisateur = Utilisateur(user=user, telephone=form.cleaned_data['telephone'], role=form.cleaned_data['role'])
            utilisateur.save()
            return redirect('connexion')
    else:
        form = FormulaireDeCreationUtilisateur()
    return render(request, 'inscription.html', {'form': form})

def liste_des_enseignants(request):
    enseignants = User.objects.filter(utilisateur__role='Enseignant')
    if request.method == 'POST':
        form = FormulaireObtentionDesID(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            request.session['enseignant_id'] = id
            return redirect('prise_de_rendez_vous')
    else:
        form = FormulaireObtentionDesID()
    return render(request, 'liste-des-enseignants.html', {'enseignants': enseignants, 'form': FormulaireObtentionDesID})

def modifier_un_rendez_vous(request):
    rendez_vous = Rendez_vous.objects.get(id=request.session['rendez_vous_id'])
    if request.method == 'POST':
        form = FormulaireDePriseDeRendezVous(request.POST)
        if form.is_valid():
            rendez_vous.update(objet=form.cleaned_data['objet'], message=form.cleaned_data['message'], date_du_rdv=form.cleaned_data['date_du_rdv'])
            return redirect('vos_rendez_vous')
    else:
        form = FormulaireDePriseDeRendezVous()
    return render(request, 'modifier-un-rendez-vous.html', {'form': FormulaireDePriseDeRendezVous(initial={'objet': rendez_vous.objet, 'date_du_rdv': rendez_vous.date_du_rdv,
    'message': rendez_vous.message})})

def modifier_vos_informations(request):
    user = User.objects.get(id=request.user.id)
    utilisateur = Utilisateur.objects.get(user_id=user.id)
    if request.method == 'POST':
        form = FormulaireDeCreationUtilisateur(request.POST)
        if form.is_valid():
            if check_password(form.cleaned_data['mot_de_passe'], user.password) == True:
                nom = form.cleaned_data['nom']
                prenom = form.cleaned_data['prenom']
                email = form.cleaned_data['email']
                telephone = form.cleaned_data['telephone']
                role = form.cleaned_data['role']

                user.update(last_name=nom, first_name=prenom, username=email, email=email)
                utilisateur.update(telephone=telephone, role=role)
                return redirect('modifier-vos-informations')
            else:
                return redirect('modifier-vos-informations')
    else:
        form = FormulaireDeCreationUtilisateur()
    return render(request, 'modifier-vos-informations.html', {'form': FormulaireDeCreationUtilisateur(initial={'nom': user.last_name, 'prenom': user.first_name, 'email': user.email, 'telephone': utilisateur.telephone, 'role': utilisateur.role})})

def prise_de_rendez_vous(request):
    enseignant = User.objects.get(id=request.session['enseignant_id'])
    if request.method == 'POST':
        form = FormulaireDePriseDeRendezVous(request.POST, request.FILES)
        if form.is_valid():
            rdv = Rendez_vous(objet=form.cleaned_data['objet'], enseignant=enseignant, eleve=request.user, fichier=request.FILES['fichier'], message=form.cleaned_data['message'], date_du_rdv=form.cleaned_data['date_du_rdv'], status='en_attente')
            rdv.save()
            return redirect('accueil')
    else:
        form = FormulaireDePriseDeRendezVous()
    return render(request, 'prise-de-rendez-vous.html', {'enseignant': enseignant, 'form': form})

def vos_rendez_vous(request):
    les_rendez_vous = Rendez_vous.objects.filter(eleve=request.user.id)
    if request.method == 'POST' and 'modifier' in request.POST:
        form = FormulaireObtentionDesID(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            request.session['rendez_vous_id'] = id
            return redirect('modifier_un_rendez_vous')
    elif request.method == 'POST' and 'supprimer' in request.POST:
        form = FormulaireObtentionDesID(request.POST)
        if form.is_valid():
            Rendez_vous.objects.filter(id=form.cleaned_data['id']).delete()
    else:
        form = FormulaireObtentionDesID()
    return render(request, 'vos-rendez-vous.html', {'les_rendez_vous': les_rendez_vous, 'form': FormulaireObtentionDesID})