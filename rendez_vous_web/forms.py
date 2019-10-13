from django import forms

CHOIX_DU_ROLE = [
    ('enseignant', 'Enseignant'),
    ('élève', 'Élève'),
]

class FormulaireDeConnexionUtilisateur(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label="Email")
    mot_de_passe = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}), label="Mot de passe")

class FormulaireDeCreationUtilisateur(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputNom', 'placeholder': 'Nom'}), max_length=100)
    prenom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputPrenom', 'placeholder': 'Prénom'}), max_length=100)
    mot_de_passe = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputMot_de_passe', 'placeholder': 'Mot de passe'}))
    confirmation_mot_de_passe = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputConfirmation_mot_de_passe', 'placeholder': 'Mot de passe'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputEmail', 'placeholder': 'Email'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputTelephone', 'placeholder': 'Téléphone'}))
    role = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'id': 'inputRole'}), choices=CHOIX_DU_ROLE)

class FormulaireDeModificationDuMotDePasse(forms.Form):
    mot_de_passe = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputMot_de_passe','placeholder': 'Mot de passe'}), label="Mot de passe")
    nouveau_mot_de_passe = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputNouveau_mot_de_passe','placeholder': 'Nouveau mot de passe'}), label="Nouveau mot de passe")
    confirmation_du_nouveau_mot_de_passe = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputConfirmation_du_nouveau_mot_de_passe','placeholder': 'Nouveau mot de passe'}), label="Nouveau mot de passe")
    
class FormulaireDePriseDeRendezVous(forms.Form):
    objet = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Objet'}), label='Objet', max_length=100)
    date_du_rdv = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'], widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'A-M-J H:M:S'}), required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '6', 'placeholder': 'Message...'}), label="Message")
    fichier = forms.FileField(required=False)

class FormulaireMessage(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '6','placeholder': 'Message...'}), label="Message")

class FormulaireMotDePasseOublie(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), label="Email")

class FormulaireObtentionDesID(forms.Form):
    id = forms.CharField(widget=forms.TextInput, label='id', max_length=100)