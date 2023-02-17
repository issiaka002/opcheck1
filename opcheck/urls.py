from django.urls import path 


from . import views

urlpatterns = [
       path( "acceuil/", views.acceuil, name='acceuil'),
       path( "", views.home),

       path( "creationCompte/", views.creationCompte,name='creationCompte'),
       
       path( "inscription/", views.incription, name='inscription'),
       path( "profil/", views.profil, name='profil'),
       
       path( "afficheProfil/", views.affiche,name='afficheProfil'),
       path( "connexion/", views.connexion,name='connexion'),
]
