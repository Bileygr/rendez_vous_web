from django.db import models
from django.contrib.auth.models import User

class Utilisateur(models.Model):
    ROLES = (
        ('A', 'Enseignant'),
        ('B', 'Elève'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLES)

class Rendez_vous(models.Model):
    STATUSES = (
        ('A', 'En attente'),
        ('B', 'Accepté'),
        ('C', 'Refusé'),
    )
    objet = models.CharField(max_length=250)
    enseignant = models.ForeignKey(Utilisateur, related_name='+', on_delete=models.PROTECT)
    eleve = models.ForeignKey(Utilisateur, related_name='+', on_delete=models.PROTECT)
    fichier = models.FileField(upload_to='uploads/')
    message = models.TextField()
    date_du_rdv = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=1, choices=STATUSES)
    dateajout = models.DateTimeField(auto_now=True)

class Message(models.Model):
    rendez_vous = models.ForeignKey(Rendez_vous, related_name='+', on_delete=models.PROTECT)
    utilisateur = models.ForeignKey(Utilisateur, related_name='+', on_delete=models.PROTECT)
    message = models.TextField()
    dateajout = models.DateTimeField(auto_now=True)