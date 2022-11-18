from django.contrib import admin

from .models import Etablissement, Rentree, Classe, Etudiant, Inscription, Enseignant, Matiere, Scolarite, Salaire, \
    Charge

# Register your models here.
admin.site.register(Rentree)
admin.site.register(Classe)
admin.site.register(Etudiant)
admin.site.register(Inscription)
admin.site.register(Enseignant)
admin.site.register(Matiere)
admin.site.register(Etablissement)
admin.site.register(Scolarite)
admin.site.register(Salaire)
admin.site.register(Charge)
