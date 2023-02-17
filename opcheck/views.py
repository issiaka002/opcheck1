

from django.shortcuts import render


def affiche(request):
      return render(request, 'affiche_profil.html')
def connexion(request):
      return render(request, 'connexion.html')



      
def creationCompte(request):
      return render(request, 'creationCompte.html')
def incription(request):
      return render(request, 'incription.html')



def profil(request):
      return render(request, 'profil.html')
def home(request):
      return render(request, 'home.html')
def acceuil(request):
      return render(request, 'acceuil.html')


