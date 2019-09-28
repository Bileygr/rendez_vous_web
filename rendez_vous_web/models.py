from django.db import models
from django.contrib.auth.models import User

class Utilisateur(models.Model):
    ROLES = (
        ('enseignant', 'Enseignant'),
        ('élève', 'Élève'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=10, null=True)
    role = models.CharField(max_length=10, choices=ROLES)

class Rendez_vous(models.Model):
    STATUSES = (
        ('en_attente', 'En attente'),
        ('accepté', 'Accepté'),
        ('refusé', 'Refusé'),
    )
    objet = models.CharField(max_length=250)
    enseignant = models.ForeignKey(User, related_name='+', on_delete=models.PROTECT)
    eleve = models.ForeignKey(User, related_name='+', on_delete=models.PROTECT)
    fichier = models.FileField(upload_to='uploads/')
    message = models.TextField()
    date_du_rdv = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=50, choices=STATUSES)
    dateajout = models.DateTimeField(auto_now=True)

class Message(models.Model):
    rendez_vous = models.ForeignKey(Rendez_vous, related_name='+', on_delete=models.PROTECT)
    utilisateur = models.ForeignKey(Utilisateur, related_name='+', on_delete=models.PROTECT)
    message = models.TextField()
    dateajout = models.DateTimeField(auto_now=True)