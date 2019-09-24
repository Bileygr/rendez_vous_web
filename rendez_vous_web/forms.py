from django import forms

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
    
class FormulaireDePriseDeRendezVous(forms.Form):
    objet = forms.CharField(widget=forms.TextInput, label='Objet', max_length=100)
    date_du_rdv = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'],widget=forms.DateTimeInput)
    message = forms.CharField(widget=forms.Textarea, label="Message")
    fichier = forms.FileField(allow_empty_file=True)

class FormulaireObtentionIDEnseignant(forms.Form):
    id = forms.CharField(widget=forms.TextInput, label='id', max_length=100)