from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from rendez_vous_web.models import Creneau
from rendez_vous_web.models import Message
from rendez_vous_web.models import Rendez_vous
from rendez_vous_web.models import Utilisateur

class FormulaireCreneau(ModelForm):
    class Meta:
        model = Creneau
        fields = ['rendez_vous', 'date', 'selection']

class FormulaireMessage(ModelForm):
    class Meta:
        model = Message
        fields = ['rendez_vous', 'utilisateur', 'message']

class FormulaireRendez_vous(ModelForm):
    class Meta:
        model = Rendez_vous
        fields = ['objet', 'enseignant', 'eleve', 'fichier', 'message', 'message_annulation', 'confirmation_enseignant', 'confirmation_eleve', 'signalement']

class FormulaireUser(ModelForm):
    class Meta:
        model = User
        fields = []

class FormulaireUtilisateur(ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['user', 'telephone', 'role']

CHOIX_DU_ROLE = [
    ('enseignant', 'Enseignant'),
    ('élève', 'Élève'),
]

class FormulaireDeConnexionUtilisateur(forms.Form):
    email = forms.EmailField(widget=forms.TextInput, label="Email")
    mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")

class FormulaireDeCreationUtilisateur(forms.Form):
    nom = forms.CharField(widget=forms.TextInput, label='Nom', max_length=100)
    prenom = forms.CharField(widget=forms.TextInput, label='Prénom', max_length=100)
    mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    email = forms.EmailField(widget=forms.TextInput, label="Email")
    telephone = forms.CharField(widget=forms.TextInput, label="Téléphone")
    role = forms.ChoiceField(widget=forms.Select, choices=CHOIX_DU_ROLE)

class FormulaireDeModificationDuMotDePasse(forms.Form):
    mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    nouveau_mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Nouveau mot de passe")
    confirmation_du_nouveau_mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Confirmation du nouveau mot de passe")
    
class FormulaireDePriseDeRendezVous(forms.Form):
    objet = forms.CharField(widget=forms.TextInput, label='Objet', max_length=100)
    date_du_rdv = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'],widget=forms.DateTimeInput)
    message = forms.CharField(widget=forms.Textarea, label="Message")
    fichier = forms.FileField(required=False)

class FormulaireMessage(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label="Message")

class FormulaireMotDePasseOublie(forms.Form):
    email = forms.EmailField(widget=forms.TextInput, label="Email")

class FormulaireObtentionDesID(forms.Form):
    id = forms.CharField(widget=forms.TextInput, label='id', max_length=100)