import django_filters
from .models import *


class ClasseFilter(django_filters.FilterSet):
    class Meta:
        model = Inscription
        fields = ['annee', 'classe']


class SalaireFilter(django_filters.FilterSet):
    class Meta:
        model = Salaire
        fields = ['annee', 'mois']



class ChargeFilter(django_filters.FilterSet):
    class Meta:
        model = Charge
        fields = ['annee', 'mois']
