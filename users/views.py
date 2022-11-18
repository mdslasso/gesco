from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, )
from django.contrib.auth.models import User
from django.urls import reverse

from apps.models import Etablissement, Classe, Etudiant, Inscription, Enseignant


def creer_users(request):
    inscriptions = Inscription.objects.all().order_by('etudiant')
    etudiants = Etudiant.objects.all().order_by('id')
    users = User.objects.all().order_by('username')
    enseignants = Enseignant.objects.all().order_by('id')
    classes = Classe.objects.all().order_by('id')
    etablissements = Etablissement.objects.all().order_by('id')[:1]

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/utilisateurs.html/")

    else:
        form = UserRegisterForm()

    return render(request, "users/ajouter_utilisateur.html",
                  {"form": form,
                   "inscriptions": inscriptions,
                   "etudiants": etudiants,
                   "enseignants": enseignants,
                   "classes": classes,
                   "etablissements": etablissements,
                   "users": users, })


class ModifierUsers(UpdateView):
    model = User
    template_name = 'users/modifier_utilisateur.html'
    fields = ["last_name", "first_name", "username", "is_superuser"]

    def get_context_data(self, *args, **kwargs):
        context = super(ModifierUsers, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['users'] = User.objects.all().order_by('username')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]

        return context

    def get_success_url(self):
        return reverse('apps:utilisateurs')


class SupprimerUsers(DeleteView):
    template_name = 'users/supprimer_utilisateur.html'
    context_object_name = 'user'
    model = User

    def get_context_data(self, *args, **kwargs):
        context = super(SupprimerUsers, self).get_context_data(*args, **kwargs)
        context['inscriptions'] = Inscription.objects.all().order_by('etudiant')
        context['etudiants'] = Etudiant.objects.all().order_by('id')
        context['users'] = User.objects.all().order_by('username')
        context['enseignants'] = Enseignant.objects.all().order_by('id')
        context['classes'] = Classe.objects.all().order_by('id')
        context['etablissements'] = Etablissement.objects.all().order_by('id')[:1]
        return context

    def get_success_url(self):
        return reverse('apps:utilisateurs')
