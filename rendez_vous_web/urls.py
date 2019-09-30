"""rendez_vous_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('accueil', views.accueil, name='accueil'),
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('inscription', views.inscription, name='inscription'),
    path('liste-des-enseignants', views.liste_des_enseignants, name='liste_des_enseignants'),
    path('modifier-un-rendez-vous', views.modifier_un_rendez_vous, name='modifier_un_rendez_vous'),
    path('modifier-vos-informations', views.modifier_vos_informations, name='modifier_vos_informations'),
    path('prise-de-rendez-vous', views.prise_de_rendez_vous, name='prise_de_rendez_vous'),
    path('vos-rendez-vous', views.vos_rendez_vous, name='vos_rendez_vous'),
    path('admin/', admin.site.urls),
]
