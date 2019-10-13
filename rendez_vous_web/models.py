from django.db import models
from django.contrib.auth.models import User

class Utilisateur(models.Model):
    ROLES = (
        ('EN', 'Enseignant'),
        ('EL', 'Élève'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=10, null=True)
    role = models.CharField(max_length=10, choices=ROLES)

class Rendez_vous(models.Model):
    STATUSES = (
        ('EA', 'En attente'),
        ('C', 'Confirmé'),
        ('D', 'Décliné'),
    )
    objet = models.CharField(max_length=250)
    enseignant = models.ForeignKey(User, related_name='+', on_delete=models.PROTECT)
    eleve = models.ForeignKey(User, related_name='+', on_delete=models.PROTECT)
    fichier = models.FileField(upload_to='uploads/')
    message = models.TextField()
    message_annulation = models.TextField(null=True)
    confirmation_enseignant = models.CharField(max_length=50, choices=STATUSES, default='EA')
    confirmation_eleve = models.CharField(max_length=50, choices=STATUSES, default='EA')
    signalement = models.BooleanField(default=False)
    dateajout = models.DateTimeField(auto_now=True)

class Creneau(models.Model):
    rendez_vous = models.ForeignKey(Rendez_vous, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False)
    selection = models.BooleanField(default=False)
    dateajout = models.DateTimeField(auto_now=True)

class Message(models.Model):
    rendez_vous = models.ForeignKey(Rendez_vous, related_name='+', on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, related_name='+', on_delete=models.CASCADE)
    message = models.TextField()
    dateajout = models.DateTimeField(auto_now=True)