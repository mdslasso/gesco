from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'apps'
urlpatterns = [

    path('home.html/', views.home, name='home'),
    path('etudiants.html/', views.Etudiants.as_view(), name='etudiants'),
    path('infos-etudiants.html/<int:pk>/', views.details_etudiants, name='details-etudiants'),

    path('badges.html/', views.Badges.as_view(), name='badges'),
    path('details_badges.html/<int:pk>/', views.details_badges, name='details_badges'),
    path('search-badges.html/', views.SearchBadge.as_view(), name='search-badges'),

    path('modifier-infos-etudiants.html/<int:pk>/', views.ModifierEtudiants.as_view(), name='modifier-etudiants'),
    path('changer-photo-etudiants.html/<int:pk>/', views.ChangerPhotoEtudiants.as_view(), name='changer-photo'),
    path('supprimer-etudiants.html/<int:pk>/', views.SupprimerEtudiant.as_view(), name='supprimer-etudiants'),

    path('enseignants.html/', views.Enseignants.as_view(), name='enseignants'),
    path('infos-enseignants.html/<int:pk>/', views.details_enseignants, name='details-enseignants'),
    path('changer-photo-enseignants.html/<int:pk>/', views.ChangerPhotoEnseignants.as_view(),
         name='changer-photo-enseignants'),
    path('modifier-infos-enseignants.html/<int:pk>/', views.ModifierEnseignants.as_view(), name='modifier-enseignants'),

    path('supprimer-enseignants.html/<int:pk>/', views.SupprimerEnseignants.as_view(), name='supprimer-enseignants'),

    path('comptabilite.html/', views.Comptabilite.as_view(), name='comptabilite'),

    path('scolarite.html/', views.Scolarites.as_view(), name='scolarites'),
    path('details-paiements.html/<int:pk>/', views.details_paiements, name='details-paiements'),
    path('effectuer-paiements.html/', views.Paiements.as_view(), name='effectuer-paiements'),
    path('modifier-paiements.html/<int:pk>/', views.ModifierPaiements.as_view(), name='modifier-paiements'),
    path('supprimer-paiements.html/<int:pk>/', views.SupprimerPaiements.as_view(), name='supprimer-paiements'),
    path('recu-paiements.html/<int:pk>/', views.RecuPaiements.as_view(), name='recu-paiements'),

    path('salaires.html/', views.salaires, name='salaires'),
    path('ajouter-salaires.html/', views.AjouterSalaires.as_view(), name='ajouter-salaires'),
    path('modifier-salaires.html/<int:pk>/', views.ModifierSalaires.as_view(), name='modifier-salaires'),
    path('supprimer-salaires.html/<int:pk>/', views.SupprimerSalaires.as_view(), name='supprimer-salaires'),
    path('imprimer-salaires.html/<int:pk>/', views.ImprimerSalaires.as_view(), name='imprimer-salaires'),

    path('charges.html/', views.charges, name='charges'),
    path('ajouter-charges.html/', views.AjouterCharges.as_view(), name='ajouter-charges'),
    path('modifier-charges.html/<int:pk>/', views.ModifierCharges.as_view(), name='modifier-charges'),
    path('supprimer-charges.html/<int:pk>/', views.SupprimerCharge.as_view(), name='supprimer-charges'),

    path('statistiques.html/', views.statistiques, name='statistiques'),

    path('inscriptions.html/', views.inscriptions, name='inscriptions'),
    path('details-inscriptions.html/<int:pk>/', views.details_inscriptions, name='details-inscriptions'),
    path('ajouter-inscription.html/', views.AjouterInscriptions.as_view(), name='ajouter-inscriptions'),
    path('modifier-inscription.html/<int:pk>/', views.ModifierInscriptions.as_view(), name='modifier-inscriptions'),
    path('supprimer-inscription.html/<int:pk>/', views.SupprimerInscription.as_view(), name='supprimer-inscriptions'),

    path('search-etudiants.html/', views.SearchEtudiant.as_view(), name='search-etudiants'),
    path('search-inscriptions.html/', views.SearchInscription.as_view(), name='search-inscriptions'),
    path('search-paiements.html/', views.SearchPaiements.as_view(), name='search-paiements'),
    path('search-enseignants.html/', views.SearchEnseignant.as_view(), name='search-enseignants'),

    path('configurations.html/', views.Configurations.as_view(), name='configurations'),
    path('configurer-etablissement.html/<int:pk>/', views.ConfigurerEtablssement.as_view(),
         name='configurer-etablissement'),
    path('rentree-scolaire.html/', views.RentreeScolaire.as_view(), name='rentree-scolaire'),
    path('infos-rentree-scolaire.html/<int:pk>/', views.InfosRentreeScolaire.as_view(), name='infos-rentree-scolaire'),
    path('ajouter-rentree-scolaire.html/', views.AjouterRentreeScolaire.as_view(), name='ajouter-rentree-scolaire'),
    path('supprimer-rentree-scolaire.html/<int:pk>/', views.SupprimerRentreeScolaire.as_view(),
         name='supprimer-rentree-scolaire'),

    path('matieres.html/', views.Matieres.as_view(), name='matieres'),
    path('ajouter-matiere.html/', views.AjouterMatieres.as_view(), name='ajouter-matiere'),
    path('modifier-matiere.html/<int:pk>/', views.ModifierMatieres.as_view(), name='modifier-matiere'),
    path('supprimer-matiere.html/<int:pk>/', views.SupprimerMatiere.as_view(), name='supprimer-matiere'),

    path('classes.html/', views.Classes.as_view(), name='classes'),
    path('ajouter-classe.html/', views.AjouterClasse.as_view(), name='ajouter-classe'),
    path('modifier-classe.html/<int:pk>/', views.ModifierClasse.as_view(), name='modifier-classe'),
    path('supprimer-classe.html/<int:pk>/', views.SupprimerClasse.as_view(), name='supprimer-classe'),

    path('utilisateurs.html/', views.Utilisateurs.as_view(), name='utilisateurs'),

    path('', auth_views.LoginView.as_view(template_name='admin/login_page.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='admin/logout_page.html'), name='logout'),

]
