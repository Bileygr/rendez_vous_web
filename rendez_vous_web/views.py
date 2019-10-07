from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from rendez_vous_web.forms import FormulaireUtilisateur
from rendez_vous_web.forms import FormulaireDeConnexionUtilisateur
from rendez_vous_web.forms import FormulaireDeCreationUtilisateur 
from rendez_vous_web.forms import FormulaireDePriseDeRendezVous
from rendez_vous_web.forms import FormulaireObtentionDesID
from rendez_vous_web.forms import FormulaireDeModificationDuMotDePasse
from rendez_vous_web.forms import FormulaireMessage
from rendez_vous_web.forms import FormulaireMotDePasseOublie
from rendez_vous_web.models import Utilisateur, Rendez_vous, Message
import random

def accueil(request):
    return render(request, 'accueil.html')

def connexion(request):
    if request.method == 'POST':
        form = FormulaireDeConnexionUtilisateur(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['mot_de_passe'])
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
        form = FormulaireUtilisateur(request.POST)
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
        form = FormulaireUtilisateur()
    return render(request, 'inscription.html', {'form': FormulaireUtilisateur()})

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

def messages_lie_au_rendez_vous(request):
    rendez_vous = Rendez_vous.objects.get(id=request.session['rendez_vous_id'])
    utilisateur = Utilisateur.objects.get(user=request.user)
    messages = Message.objects.filter(rendez_vous=rendez_vous).order_by('dateajout')
    if request.method == 'POST':
        form = FormulaireMessage(request.POST)
        if form.is_valid():
            message = Message(rendez_vous=rendez_vous, utilisateur=utilisateur, message=form.cleaned_data['message'])
            message.save()
    else:
        form = FormulaireMessage()
    return render(request, 'messages-lie-au-rendez-vous.html', {'form': FormulaireMessage(), 'messages': messages, 'objet': rendez_vous.objet, 'date_du_rdv': rendez_vous.date_du_rdv, 'fichier': rendez_vous.fichier})

def modifier_un_rendez_vous(request):
    rendez_vous = Rendez_vous.objects.get(id=request.session['rendez_vous_id'])
    if request.method == 'POST':
        form = FormulaireDePriseDeRendezVous(request.POST, request.FILES)
        if form.is_valid():
            rendez_vous.objet = form.cleaned_data['objet'] 
            rendez_vous.message = form.cleaned_data['message']
            rendez_vous.date_du_rdv = form.cleaned_data['date_du_rdv']

            if 'fichier' in request.FILES:
                rendez_vous.fichier = request.FILES['fichier']

            rendez_vous.save()
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
                user.last_name = form.cleaned_data['nom']
                user.first_name = form.cleaned_data['prenom']
                user.email = form.cleaned_data['email']
                utilisateur.telephone = form.cleaned_data['telephone']
                utilisateur.role = form.cleaned_data['role']

                user.save()
                utilisateur.save()
                return redirect('modifier_vos_informations')
            else:
                return redirect('modifier_vos_informations')
    else:
        form = FormulaireDeCreationUtilisateur()
    return render(request, 'modifier-vos-informations.html', {'form': FormulaireDeCreationUtilisateur(initial={'nom': user.last_name, 'prenom': user.first_name, 'email': user.email, 'telephone': utilisateur.telephone, 'role': utilisateur.role})})

def modifier_votre_mot_de_passe(request):
    if request.method == 'POST':
        form = FormulaireDeModificationDuMotDePasse(request.POST)
        if form.is_valid():
            if check_password(form.cleaned_data['mot_de_passe'], request.user.password):
                if form.cleaned_data['nouveau_mot_de_passe'] == form.cleaned_data['confirmation_du_nouveau_mot_de_passe']:
                    request.user.set_password(form.cleaned_data['nouveau_mot_de_passe'])
                    request.user.save()
                    return redirect('deconnexion')
                else:
                  return redirect('modifier-votre-mot-de-passe')  
    else:
        form = FormulaireDeModificationDuMotDePasse()
    return render(request, 'modifier-votre-mot-de-passe.html', {'form': FormulaireDeModificationDuMotDePasse()})

def mot_de_passe_oublie(request):
    if request.method == 'POST':
        form = FormulaireMotDePasseOublie(request.POST)
        if form.is_valid():
            caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\/|!@#$%?&*()_+ÀÇ¨È:É\"'{}[]-=àç^è;é.,"
            mot_de_passe = ""
            for c in range(16):
                mot_de_passe += random.choice(caracteres)
            user = User.objects.get(email=form.cleaned_data['email'])
            user.set_password(mot_de_passe)
            user.save()
            print(mot_de_passe)
            send_mail('Réinitialisation de votre mot de passe', 'Votre nouveau mot de passe est '+mot_de_passe+' veuillez le changer une fois connecté.', 'chesirkeirendezvousapp@gmail.com', [form.cleaned_data['email']], fail_silently=False,)
            return redirect('accueil')
    else:
        form = FormulaireMotDePasseOublie()
    return render(request, 'mot-de-passe-oublie.html', {'form': FormulaireMotDePasseOublie()})

def prise_de_rendez_vous(request):
    enseignant = User.objects.get(id=request.session['enseignant_id'])
    if request.method == 'POST':
        form = FormulaireDePriseDeRendezVous(request.POST, request.FILES)
        if form.is_valid():
            rdv = Rendez_vous(objet=form.cleaned_data['objet'], enseignant=enseignant, eleve=request.user, message=form.cleaned_data['message'], date_du_rdv=form.cleaned_data['date_du_rdv'], status='en_attente')
            if 'fichier' in request.FILES:
                rdv.fichier = request.FILES['fichier']
            rdv.save()
            return redirect('accueil')
    else:
        form = FormulaireDePriseDeRendezVous()
    return render(request, 'prise-de-rendez-vous.html', {'enseignant': enseignant, 'form': form})

def vos_rendez_vous(request):
    les_rendez_vous = Rendez_vous.objects.filter(Q(eleve=request.user.id) | Q(enseignant=request.user.id))
    if request.method == 'POST' and 'message' in request.POST:
        form = FormulaireObtentionDesID(request.POST)
        if form.is_valid():
            request.session['rendez_vous_id'] = form.cleaned_data['id']
            return redirect('messages_lie_au_rendez_vous')
    elif request.method == 'POST' and 'modifier' in request.POST:
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