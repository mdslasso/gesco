from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from itertools import chain
from django.db.models import Avg, Max, Min, Sum
from django.shortcuts import render, redirect
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, )
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from .filters import *
from django.contrib.auth.models import User


def erreur_404(request, exception):
    return render(request, 'apps/erreur_404.html')


def home(request):
    return render(request, 'apps/home.html')


# --------------------------------ETUDIANTS-----------------------------------


class Etudiants(SuccessMessageMixin, CreateView):
    model = Etudiant
    template_name = 'apps/etudiants.html'
    fields = ['nom', 'prenom', 'naissance', 'lieu', 'pere', 'mere', 'matricule', 'numero', 'urgent']
    success_message = "L'étudiant a été enregistré avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(Etudiants, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants_home'] = Etudiant.objects.all().order_by('-id')[:9]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['dernier_etudiant'] = Etudiant.objects.all().order_by('-id')[:1]
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


def details_etudiants(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    etudiants = Etudiant.objects.all().order_by('id')
    inscriptions = Inscription.objects.all().order_by('id')
    inscriptions_confirm = Inscription.objects.all().order_by('id')[:1]
    scolarites = Scolarite.objects.all().order_by('id')
    etablissements = Etablissement.objects.all().order_by('id')[:1]
    classes = Classe.objects.all().order_by('id')
    enseignants = Enseignant.objects.all().order_by('prenom')

    context = {
        'etudiant': etudiant,
        'etudiants': etudiants,
        'inscriptions': inscriptions,
        'inscriptions_confirm': inscriptions_confirm,
        'scolarites': scolarites,
        'etablissements': etablissements,
        'classes': classes,
        'enseignants': enseignants,
    }

    return render(request, 'apps/details_etudiants.html', context)


class ModifierEtudiants(SuccessMessageMixin, UpdateView):
    model = Etudiant
    template_name = 'operations/modifier_etudiants.html'
    fields = ['nom', 'prenom', 'naissance', 'lieu', 'pere', 'mere', 'matricule', 'numero', 'urgent']
    success_message = "La modification a été effectué avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(ModifierEtudiants, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class ChangerPhotoEtudiants(SuccessMessageMixin, UpdateView):
    model = Etudiant
    template_name = 'operations/modifier_photo_etudiant.html'
    fields = ['photo']
    success_message = "La photo a été changée avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(ChangerPhotoEtudiants, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class SupprimerEtudiant(DeleteView):
    model = Etudiant
    template_name = 'operations/supprimer_etudiants.html'

    def get_success_url(self):
        return reverse('apps:etudiants')

    def get_context_data(self, *args, **kwargs):
        context = super(SupprimerEtudiant, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


# --------------------------------ETUDIANTS-----------------------------------


# --------------------------------ENSEIGNANTS-----------------------------------


class Enseignants(SuccessMessageMixin, CreateView):
    model = Enseignant
    template_name = 'apps/enseignants.html'
    fields = ['prenom', 'nom', 'naissance', 'numero', 'matricule', 'matiere', 'classe']

    success_message = "L'enseignant a été ajouté avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(Enseignants, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['dernier_enseignant'] = Enseignant.objects.all().order_by('-id')[:1]
        context['classes'] = Classe.objects.all().order_by('id')
        context['matieres'] = Matiere.objects.all().order_by('matiere')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


def details_enseignants(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    etudiants = Etudiant.objects.all().order_by('id')
    inscriptions = Inscription.objects.all().order_by('id')
    inscriptions_confirm = Inscription.objects.all().order_by('id')[:1]
    scolarites = Scolarite.objects.all().order_by('id')
    etablissements = Etablissement.objects.all().order_by('id')[:1]
    classes = Classe.objects.all().order_by('id')
    enseignants = Enseignant.objects.all().order_by('prenom')

    context = {
        'enseignant': enseignant,
        'etudiants': etudiants,
        'inscriptions': inscriptions,
        'inscriptions_confirm': inscriptions_confirm,
        'scolarites': scolarites,
        'etablissements': etablissements,
        'classes': classes,
        'enseignants': enseignants,
    }

    return render(request, 'apps/details_enseignants.html', context)


class ModifierEnseignants(SuccessMessageMixin, UpdateView):
    model = Enseignant
    template_name = 'operations/modifier_enseignants.html'
    fields = ['prenom', 'nom', 'naissance', 'numero', 'matricule', 'matiere', 'classe']

    success_message = "L'enseignant a été modifié avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(ModifierEnseignants, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class ChangerPhotoEnseignants(SuccessMessageMixin, UpdateView):
    model = Enseignant
    template_name = 'operations/modifier_photo_enseignant.html'
    fields = ['photo']
    success_message = "La photo a été changée avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(ChangerPhotoEnseignants, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class SupprimerEnseignants(DeleteView):
    model = Enseignant
    template_name = 'operations/supprimer_enseignants.html'

    def get_success_url(self):
        return reverse('apps:enseignants')

    def get_context_data(self, *args, **kwargs):
        context = super(SupprimerEnseignants, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


# --------------------------------ENSEIGNANTS-----------------------------------


# --------------------------------INSCRIPTIONS-----------------------------------


def inscriptions(request):
    annees = Rentree.objects.all().order_by('-id')
    inscriptions = Inscription.objects.all().order_by('annee')
    inscriptions_home = Inscription.objects.all().order_by('annee')[:10]
    etudiants = Etudiant.objects.all().order_by('id')
    classes = Classe.objects.all().order_by('id')
    etablissements = Etablissement.objects.all().order_by('id')[:1]
    enseignants = Enseignant.objects.all().order_by('prenom')

    inscriptions_filters = Inscription.objects.all().order_by('etudiant')
    myFilter = ClasseFilter(request.GET, queryset=inscriptions_filters)
    inscriptions_filters = myFilter.qs

    context = {
        'annees': annees,
        'inscriptions': inscriptions,
        'inscriptions_home': inscriptions_home,
        'etudiants': etudiants,
        'etablissements': etablissements,
        'classes': classes,
        'myFilter': myFilter,
        'enseignants': enseignants,
        'inscriptions_filters': inscriptions_filters,
    }

    return render(request, 'apps/inscriptions.html', context)


def details_inscriptions(request, pk):
    inscrit = get_object_or_404(Inscription, pk=pk)
    inscriptions = Inscription.objects.all().order_by('id')
    etudiants = Etudiant.objects.all().order_by('id')
    scolarites = Scolarite.objects.all().order_by('id')
    enseignants = Enseignant.objects.all().order_by('prenom')
    etablissements = Etablissement.objects.all().order_by('id')[:1]
    classes = Classe.objects.all().order_by('id')
    total_payement = Scolarite.objects.filter(etudiant=inscrit.id).aggregate(Sum('payement'))
    payements = Scolarite.objects.filter(etudiant=inscrit.id).values()

    context = {
        'inscrit': inscrit,
        'inscriptions': inscriptions,
        'etudiants': etudiants,
        'scolarites': scolarites,
        'total_payement': total_payement,
        'payements': payements,
        'etablissements': etablissements,
        'classes': classes,
        'enseignants': enseignants, }

    return render(request, 'apps/details_inscriptions.html', context)


class AjouterInscriptions(SuccessMessageMixin, CreateView):
    model = Inscription
    template_name = 'operations/ajouter_inscriptions.html'
    fields = ['annee', 'etudiant', 'classe', 'scolarite', 'date']
    success_message = "L'inscription a été effectué avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(AjouterInscriptions, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['annees'] = Rentree.objects.all().order_by('-id')
        context['classes'] = Classe.objects.all().order_by('-id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class ModifierInscriptions(SuccessMessageMixin, UpdateView):
    model = Inscription
    template_name = 'operations/modifier_inscriptions.html'
    fields = ['annee', 'etudiant', 'classe', 'scolarite', 'date']
    success_message = "La modification a été effectué avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(ModifierInscriptions, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['annees'] = Rentree.objects.all().order_by('-id')
        context['classes'] = Classe.objects.all().order_by('-id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class SupprimerInscription(DeleteView):
    model = Inscription
    template_name = 'operations/supprimer_inscriptions.html'

    def get_success_url(self):
        return reverse('apps:inscriptions')

    def get_context_data(self, *args, **kwargs):
        context = super(SupprimerInscription, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['rentrees'] = Rentree.objects.all().order_by('-id')
        context['classes'] = Classe.objects.all().order_by('-id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


# --------------------------------INSCRIPTIONS-----------------------------------


# --------------------------------COMPTABILITES-----------------------------------


class Comptabilite(ListView):
    model = Scolarite
    template_name = 'comptabilites/comptabilite.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Comptabilite, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class Scolarites(ListView):
    model = Scolarite
    context_object_name = 'scolarites'
    template_name = 'comptabilites/scolarites.html'
    ordering = ['annee']

    def get_context_data(self, *args, **kwargs):
        context = super(Scolarites, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


def details_paiements(request, pk):
    inscrit = get_object_or_404(Inscription, pk=pk)
    inscriptions = Inscription.objects.all().order_by('etudiant')[:100]
    etudiants = Etudiant.objects.all().order_by('id')
    enseignants = Enseignant.objects.all().order_by('id')
    scolarites = Scolarite.objects.all().order_by('id')
    classes = Classe.objects.all().order_by('id')
    etablissements = Etablissement.objects.all().order_by('id')[:1]
    total_payement = Scolarite.objects.filter(etudiant=inscrit.id).aggregate(Sum('payement'))
    payements = Scolarite.objects.filter(etudiant=inscrit.id).values()

    return render(request, 'comptabilites/details_paiements.html',
                  {'inscrit': inscrit,
                   'inscriptions': inscriptions,
                   'etudiants': etudiants,
                   'scolarites': scolarites,
                   'total_payement': total_payement,
                   'payements': payements,
                   'etablissements': etablissements,
                   'classes': classes,
                   'enseignants': enseignants,
                   })


class Paiements(SuccessMessageMixin, CreateView):
    model = Scolarite
    template_name = 'comptabilites/ajouter_paiements.html'
    ordering = ['annee']
    fields = ['annee', 'mois', 'etudiant', 'payement', 'date']
    success_message = "Le Paiement a été effectué avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(Paiements, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class ModifierPaiements(SuccessMessageMixin, UpdateView):
    model = Scolarite
    template_name = 'comptabilites/modifier_paiements.html'
    ordering = ['annee']
    fields = ['annee', 'mois', 'etudiant', 'payement', 'date']
    success_message = "La modification a été effectué avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(ModifierPaiements, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class SupprimerPaiements(DeleteView):
    model = Scolarite
    template_name = 'comptabilites/supprimer_paiements.html'

    def get_success_url(self):
        return reverse('apps:details-paiements', args=[self.object.etudiant.id])

    def get_context_data(self, *args, **kwargs):
        context = super(SupprimerPaiements, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class RecuPaiements(DetailView):
    model = Scolarite
    context_object_name = 'recu'
    template_name = 'comptabilites/recus_scolarites.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RecuPaiements, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context




def salaires(request):
    annees = Rentree.objects.all().order_by('-id')
    inscriptions = Inscription.objects.all().order_by('annee')
    salaires = Salaire.objects.all().order_by('-id')
    etudiants = Etudiant.objects.all().order_by('id')
    classes = Classe.objects.all().order_by('id')
    etablissements = Etablissement.objects.all().order_by('id')[:1]
    enseignants = Enseignant.objects.all().order_by('prenom')

    salaires_filters = Salaire.objects.all().order_by('-id')
    myFilter = SalaireFilter(request.GET, queryset=salaires_filters)
    salaires_filters = myFilter.qs

    context = {
        'annees': annees,
        'inscriptions': inscriptions,
        'etudiants': etudiants,
        'etablissements': etablissements,
        'classes': classes,
        'myFilter': myFilter,
        'enseignants': enseignants,
        'salaires_filters': salaires_filters,
        'salaires': salaires,
    }

    return render(request, 'comptabilites/salaires.html', context)

class AjouterSalaires(CreateView):
    model = Salaire
    template_name = 'comptabilites/ajouter_salaires.html'
    fields=['annee', 'mois', 'enseignant', 'salaire', 'date']

    def get_context_data(self, *args, **kwargs):
        context = super(AjouterSalaires, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context

class ModifierSalaires(SuccessMessageMixin, UpdateView):
    model = Salaire
    template_name = 'comptabilites/modifier_salaires.html'
    fields=['annee', 'mois', 'enseignant', 'salaire', 'date']
    success_message = "La modification a été effectué avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(ModifierSalaires, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class SupprimerSalaires(DeleteView):
    model = Salaire
    template_name = 'comptabilites/supprimer_salaires.html'

    def get_success_url(self):
        return reverse('apps:salaires')


    def get_context_data(self, *args, **kwargs):
        context = super(SupprimerSalaires, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class ImprimerSalaires(DetailView):
    model = Salaire
    template_name = 'comptabilites/recus_salaires.html'
    context_object_name = 'recu'

    def get_context_data(self, *args, **kwargs):
        context = super(ImprimerSalaires, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context




def charges(request):
    annees = Rentree.objects.all().order_by('-id')
    inscriptions = Inscription.objects.all().order_by('annee')
    charges = Charge.objects.all().order_by('-id')
    etudiants = Etudiant.objects.all().order_by('id')
    classes = Classe.objects.all().order_by('id')
    etablissements = Etablissement.objects.all().order_by('id')[:1]
    enseignants = Enseignant.objects.all().order_by('prenom')

    charges_filters = Charge.objects.all().order_by('-id')
    myFilter = ChargeFilter(request.GET, queryset=charges_filters)
    charges_filters = myFilter.qs

    context = {
        'annees': annees,
        'inscriptions': inscriptions,
        'etudiants': etudiants,
        'etablissements': etablissements,
        'classes': classes,
        'myFilter': myFilter,
        'enseignants': enseignants,
        'charges_filters': charges_filters,
        'charges': charges,
    }

    return render(request, 'comptabilites/charges.html', context)



class AjouterCharges(SuccessMessageMixin,CreateView):
    model = Charge
    template_name = 'comptabilites/ajouter_charges.html'
    fields =['annee', 'mois', 'commentaire', 'montant', 'date']

    success_message = "La charge a été enregistrée avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(AjouterCharges, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context



class ModifierCharges(SuccessMessageMixin,UpdateView):
    model = Charge
    template_name = 'comptabilites/modifier_charges.html'
    fields =['annee', 'mois', 'commentaire', 'montant', 'date']
    success_message = "Charge modifiée avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(ModifierCharges, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context

class SupprimerCharge(SuccessMessageMixin,DeleteView):
    model = Charge
    template_name = 'comptabilites/supprimer_charges.html'


    def get_success_url(self):
        return reverse('apps:charges')


# --------------------------------COMPTABILITES-----------------------------------







# --------------------------------BADGES-----------------------------------


class Badges(ListView):
    model = Etudiant
    context_object_name = 'etudiants'
    template_name = 'apps/badges.html'
    ordering = ['prenom']

    def get_context_data(self, *args, **kwargs):
        context = super(Badges, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all()
        context['etudiants_home'] = Etudiant.objects.all().order_by('id').order_by('prenom')[:100]
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


def details_badges(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    etudiants = Etudiant.objects.all().order_by('id')
    etudiants_home = Etudiant.objects.all().order_by('id').order_by('prenom')[:100]
    inscriptions = Inscription.objects.all().order_by('id')
    inscriptions_confirm = Inscription.objects.all().order_by('id')[:1]
    scolarites = Scolarite.objects.all().order_by('id')
    etablissements = Etablissement.objects.all().order_by('id')[:1]
    classes = Classe.objects.all().order_by('id')
    enseignants = Enseignant.objects.all().order_by('prenom')

    context = {
        'etudiant': etudiant,
        'etudiants': etudiants,
        'inscriptions': inscriptions,
        'inscriptions_confirm': inscriptions_confirm,
        'scolarites': scolarites,
        'etablissements': etablissements,
        'classes': classes,
        'etudiants_home': etudiants_home,
        'enseignants': enseignants,
    }

    return render(request, 'apps/details_badges.html', context)


# --------------------------------BADGES-----------------------------------


# --------------------------------CONFIGURATIONS-----------------------------------


class Configurations(ListView):
    model = Scolarite
    context_object_name = 'scolarites'
    template_name = 'configurations/configurations.html'
    ordering = ['annee']

    def get_context_data(self, *args, **kwargs):
        context = super(Configurations, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]
        context['rentrees'] = Rentree.objects.all().order_by('id')[:1]

        return context


class ConfigurerEtablssement(SuccessMessageMixin, UpdateView):
    model = Etablissement
    fields = ['nom', 'numero', 'email', 'adresse', 'directeur', 'logo']
    template_name = 'configurations/modifier_etablissement.html'
    success_message = "La modification de l'établissement a été effectué avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(ConfigurerEtablssement, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]
        context['rentrees'] = Rentree.objects.all().order_by('id')[:1]

        return context


class RentreeScolaire(ListView):
    model = Rentree
    context_object_name = 'rentrees'
    template_name = 'configurations/rentree_scolaire.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(RentreeScolaire, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class InfosRentreeScolaire(SuccessMessageMixin, UpdateView):
    model = Rentree
    context_object_name = 'rentre'
    template_name = 'configurations/modifier_rentree_scolaire.html'
    success_message = "La modification a  été effectuée avec succès"
    fields = ['annee', 'debut_inscription', 'fin_inscription', 'debut_cours', 'fin_cours']

    def get_context_data(self, *args, **kwargs):
        context = super(InfosRentreeScolaire, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['rentrees'] = Rentree.objects.all().order_by('-id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class AjouterRentreeScolaire(SuccessMessageMixin, CreateView):
    model = Rentree
    template_name = 'configurations/ajouter_rentree_scolaire.html'
    success_message = "L'ajout a  été effectué avec succès"
    fields = ['annee', 'debut_inscription', 'fin_inscription', 'debut_cours', 'fin_cours']

    def get_context_data(self, *args, **kwargs):
        context = super(AjouterRentreeScolaire, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['rentrees'] = Rentree.objects.all().order_by('-id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class SupprimerRentreeScolaire(SuccessMessageMixin, DeleteView):
    model = Rentree
    template_name = 'configurations/supprimer_rentree_scolaire.html'
    success_message = "La suppression a  été effectué avec succès"

    def get_success_url(self):
        return reverse('apps:rentree-scolaire')

    def get_context_data(self, *args, **kwargs):
        context = super(SupprimerRentreeScolaire, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['rentrees'] = Rentree.objects.all().order_by('-id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class Matieres(ListView):
    model = Matiere
    context_object_name = 'matieres'
    template_name = 'configurations/matieres.html'
    ordering = ['matiere']

    def get_context_data(self, *args, **kwargs):
        context = super(Matieres, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class AjouterMatieres(SuccessMessageMixin, CreateView):
    model = Matiere
    template_name = 'configurations/ajouter_matiere.html'
    fields = ['matiere']
    success_message = "L'ajout a été effectuée avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(AjouterMatieres, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['matieres'] = Matiere.objects.all().order_by('matiere')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class ModifierMatieres(SuccessMessageMixin, UpdateView):
    model = Matiere
    context_object_name = 'matiere'
    template_name = 'configurations/modifier_matiere.html'
    fields = ['matiere']
    success_message = "La modification a  été effectuée avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(ModifierMatieres, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['matieres'] = Matiere.objects.all().order_by('matiere')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class SupprimerMatiere(SuccessMessageMixin, DeleteView):
    model = Matiere
    template_name = 'configurations/supprimer_matiere.html'
    success_message = "La suppression a  été effectuée avec succès"

    def get_success_url(self):
        return reverse('apps:matieres')

    def get_context_data(self, *args, **kwargs):
        context = super(SupprimerMatiere, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['rentrees'] = Rentree.objects.all().order_by('-id')
        context['matieres'] = Matiere.objects.all().order_by('matiere')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class Classes(ListView):
    model = Classe
    context_object_name = 'classes'
    template_name = 'configurations/classes.html'
    ordering = ['classe']

    def get_context_data(self, *args, **kwargs):
        context = super(Classes, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class AjouterClasse(SuccessMessageMixin, CreateView):
    model = Classe
    context_object_name = 'classe'
    template_name = 'configurations/ajouter_classe.html'
    fields = ['classe']
    success_message = "L'ajout a  été effectuée avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(AjouterClasse, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class ModifierClasse(SuccessMessageMixin, UpdateView):
    model = Classe
    context_object_name = 'classe'
    template_name = 'configurations/modifier_classe.html'
    fields = ['classe']
    success_message = "La modification a  été effectuée avec succès"

    def get_context_data(self, *args, **kwargs):
        context = super(ModifierClasse, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


class SupprimerClasse(SuccessMessageMixin, DeleteView):
    model = Classe
    context_object_name = 'classe'
    template_name = 'configurations/supprimer_classe.html'
    fields = ['classe']
    success_message = "La suppression a été effectuée avec succès"

    def get_success_url(self):
        return reverse('apps:classes')

    def get_context_data(self, *args, **kwargs):
        context = super(SupprimerClasse, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context


# --------------------------------CONFIGURATIONS-----------------------------------


# --------------------------------SEARCH-----------------------------------


class SearchEtudiant(ListView):
    model = Etudiant
    template_name = 'apps/etudiants.html'
    context_object_name = 'etudiants'
    paginate_by = 15
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super(SearchEtudiant, self).get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            prenom_results = Etudiant.objects.filter(Q(prenom__icontains=query))
            nom_results = Etudiant.objects.filter(Q(nom__icontains=query))
            numero_results = Etudiant.objects.filter(Q(numero__icontains=query))
            matricule_results = Etudiant.objects.filter(Q(matricule__icontains=query))
            queryset_chain = chain(prenom_results, nom_results, numero_results, matricule_results)

            qs = sorted(queryset_chain, key=lambda instance: instance.pk, reverse=True)
            self.count = len(qs)
            return qs

        return Etudiant.objects.none()


class SearchEnseignant(ListView):
    model = Enseignant
    template_name = 'apps/enseignants.html'
    context_object_name = 'enseignants'
    paginate_by = 10
    count = 0
    fields = ['prenom', 'nom', 'naissance', 'numero', 'matricule', 'matiere', 'classe']

    def get_context_data(self, *args, **kwargs):
        context = super(SearchEnseignant, self).get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['matieres'] = Matiere.objects.all().order_by('matiere')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            prenom_results = Enseignant.objects.filter(Q(prenom__icontains=query))
            nom_results = Enseignant.objects.filter(Q(nom__icontains=query))
            numero_results = Enseignant.objects.filter(Q(numero__icontains=query))
            matricule_results = Enseignant.objects.filter(Q(matricule__icontains=query))
            queryset_chain = chain(prenom_results, nom_results, numero_results, matricule_results)

            qs = sorted(queryset_chain, key=lambda instance: instance.pk, reverse=True)
            self.count = len(qs)
            return qs

        return Enseignant.objects.none()


class SearchInscription(ListView):
    model = Inscription
    template_name = 'apps/search_inscriptions.html'
    context_object_name = 'inscriptions'
    paginate_by = 15
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super(SearchInscription, self).get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['annees'] = Rentree.objects.all().order_by('-id')
        context['classes'] = Classe.objects.all().order_by('-id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            prenom_results = Inscription.objects.filter(Q(etudiant__prenom__icontains=query))
            nom_results = Inscription.objects.filter(Q(etudiant__nom__icontains=query))
            numero_results = Inscription.objects.filter(Q(etudiant__numero__icontains=query))
            matricule_results = Inscription.objects.filter(Q(etudiant__matricule__icontains=query))
            queryset_chain = chain(prenom_results, nom_results, numero_results, matricule_results)

            qs = sorted(queryset_chain, key=lambda instance: instance.pk, reverse=True)
            self.count = len(qs)
            return qs

        return Inscription.objects.none()


class SearchPaiements(ListView):
    model = Inscription
    template_name = 'apps/scolarites.html'
    paginate_by = 15
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super(SearchPaiements, self).get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['annees'] = Rentree.objects.all().order_by('-id')
        context['classes'] = Classe.objects.all().order_by('-id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            prenom_results = Inscription.objects.filter(Q(etudiant__prenom__icontains=query))
            nom_results = Inscription.objects.filter(Q(etudiant__nom__icontains=query))
            numero_results = Inscription.objects.filter(Q(etudiant__numero__icontains=query))
            matricule_results = Inscription.objects.filter(Q(etudiant__matricule__icontains=query))
            queryset_chain = chain(prenom_results, nom_results, numero_results, matricule_results)

            qs = sorted(queryset_chain, key=lambda instance: instance.pk, reverse=True)
            self.count = len(qs)
            return qs

        return Inscription.objects.none()


class SearchBadge(ListView):
    model = Etudiant
    template_name = 'apps/badges.html'
    context_object_name = 'etudiants'
    paginate_by = 15
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super(SearchBadge, self).get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        context['inscriptions'] = Inscription.objects.all().order_by('id')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['etudiants_home'] = Etudiant.objects.all().order_by('id').order_by('prenom')[:100]
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            prenom_results = Etudiant.objects.filter(Q(prenom__icontains=query))
            nom_results = Etudiant.objects.filter(Q(nom__icontains=query))
            numero_results = Etudiant.objects.filter(Q(numero__icontains=query))
            matricule_results = Etudiant.objects.filter(Q(matricule__icontains=query))
            queryset_chain = chain(prenom_results, nom_results, numero_results, matricule_results)

            qs = sorted(queryset_chain, key=lambda instance: instance.pk, reverse=True)
            self.count = len(qs)
            return qs

        return Etudiant.objects.none()


# --------------------------------SEARCH-----------------------------------


# --------------------------------ADMIN-----------------------------------

class Utilisateurs(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'configurations/utilisateurs.html'
    ordering = ['username']

    def get_context_data(self, *args, **kwargs):
        context = super(Utilisateurs, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')[:100]
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context

# --------------------------------ADMIN-----------------------------------
