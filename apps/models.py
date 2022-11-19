from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

Mois = (
    ("Janvier", "Janvier"), ("Fevrier", "Fevrier"), ("Mars", "Mars"), ("Avril", "Avril"), ("Mai", "Mai"),
    ("Juin", "Juin")
    , ("Juillet", "Juillet"), ("Août", "Août"), ("Septembre", "Septembre"),
    ("Octobre", "Octobre"), ("Novembre", "Novembre"), ("Decembre", "Decembre")
)


class Rentree(models.Model):
    annee = models.CharField(max_length=250, verbose_name="Année Scolaire", unique=True, default="2000-2000")
    debut_inscription = models.CharField(max_length=250, verbose_name="Début d'inscription", unique=True, default="00.00.2000")
    fin_inscription = models.CharField(max_length=250, verbose_name="fin d'inscription", unique=True,default="00.00.2000")
    debut_cours = models.CharField(max_length=250, verbose_name="Début des cours", unique=True, default="00.00.2000")
    fin_cours = models.CharField(max_length=250, verbose_name="Fin des cours", unique=True, default="00.00.2000")
    slug = AutoSlugField(populate_from='annee', unique=True)

    class Meta:
        ordering = ('-id',)

    def get_absolute_url(self):
        return reverse('apps:rentree-scolaire')

    def __str__(self):
        return str(self.annee)


class Etablissement(models.Model):
    nom = models.CharField(max_length=250, verbose_name=" Nom de l'établissement")
    numero = models.CharField(max_length=250, verbose_name="Numéro")
    email = models.CharField(max_length=250, verbose_name="E-mail")
    adresse = models.CharField(max_length=250, verbose_name="Adresse")
    directeur = models.CharField(max_length=250, verbose_name="Nom du directeur")
    logo = models.ImageField(upload_to='Photo/images', verbose_name="Choisir le logo", blank=True)

    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse('apps:configurations')

    def __str__(self):
        return str(self.nom)


class Classe(models.Model):
    classe = models.CharField(max_length=250, verbose_name="Classes", unique=True, default="")
    slug = AutoSlugField(populate_from='classe', unique=True)

    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse('apps:classes')

    def __str__(self):
        return str(self.classe)


class Matiere(models.Model):
    matiere = models.CharField(max_length=250, verbose_name="Matières", unique=True, default="")
    slug = AutoSlugField(populate_from='matiere', unique=True)

    def get_absolute_url(self):
        return reverse('apps:matieres')

    class Meta:
        ordering = ('matiere',)

    def __str__(self):
        return str(self.matiere)


class Etudiant(models.Model):
    nom = models.CharField(max_length=250, verbose_name="Nom")
    prenom = models.CharField(max_length=250, verbose_name="Prénom")
    naissance = models.CharField(max_length=250, verbose_name="Date de naissance", default="01.01.2022")
    lieu = models.CharField(max_length=250, verbose_name="Lieu de naissance")
    pere = models.CharField(max_length=250, verbose_name="Nom du père ")
    mere = models.CharField(max_length=250, verbose_name="Nom de la mère")
    numero = models.CharField(max_length=250, verbose_name="Numéro", blank=True, unique=True)
    urgent = models.CharField(max_length=250, verbose_name="Numéro à contacter en cas d'urgence")
    matricule = models.IntegerField(verbose_name="Matricule", unique=True, null=True)
    photo = models.ImageField(upload_to='Photo/images', verbose_name="Choisir la photo", blank=True)

    def get_absolute_url(self):
        return reverse('apps:details-etudiants', args=[self.id])

    class Meta:
        ordering = ('prenom',)

    def __str__(self):
        return str(self.prenom + ' ' + self.nom + ' - Matricule : ' + str(self.matricule))


class Inscription(models.Model):
    annee = models.ForeignKey(Rentree, on_delete=models.CASCADE, null=True, verbose_name="Année Scolaire", default='')
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True, verbose_name="Étudiants", default='')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True, verbose_name="Classes", default='')
    scolarite = models.IntegerField(verbose_name="Scolarite (GNF)")
    date = models.CharField(max_length=250, verbose_name="Date d'inscription", default="01.01.2022")

    def get_absolute_url(self):
        return reverse('apps:inscriptions')

    class Meta:
        ordering = ('etudiant',)

    def __str__(self):
        return str(self.etudiant) + " - Année : " + str(self.annee)


class Scolarite(models.Model):
    annee = models.ForeignKey(Rentree, on_delete=models.CASCADE, null=True, verbose_name="Année Scolaire", default='',related_name="rentree")
    mois = models.CharField(max_length=250, choices=Mois, default=1, verbose_name="Mois")
    etudiant = models.ForeignKey(Inscription, on_delete=models.CASCADE, verbose_name="Étudiants", default='', related_name="inscription")
    payement = models.IntegerField(verbose_name="Paiement (GNF)")
    date = models.CharField(max_length=250, verbose_name="Date du Paiement", default="01.01.2022")

    def get_absolute_url(self):
        return reverse('apps:details-paiements', args=[self.etudiant.id])

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.etudiant)


class Enseignant(models.Model):
    nom = models.CharField(max_length=250, verbose_name="Nom")
    prenom = models.CharField(max_length=250, verbose_name="Prénom")
    naissance = models.CharField(max_length=250, verbose_name="Date de naissance", default="01.01.2022")
    numero = models.CharField(max_length=250, verbose_name="Numero", unique=True)
    matricule = models.IntegerField(verbose_name="Matricule", unique=True, null=True)
    matiere = models.ManyToManyField(Matiere, verbose_name="Matières", related_name='area')
    classe = models.ManyToManyField(Classe, verbose_name="Classes")
    photo = models.ImageField(upload_to='Photo/images', verbose_name="Choisir la photo", blank=True)

    def get_absolute_url(self):
        return reverse('apps:details-enseignants', args=[self.id])


    class Meta:
        ordering = ('prenom',)

    def __str__(self):
        return str(
            self.prenom + ' ' + self.nom + ' - Matircule : ' + str(self.matricule) + ' - Numero : ' + self.numero)


class Salaire(models.Model):
    annee = models.ForeignKey(Rentree, on_delete=models.CASCADE, null=True, verbose_name="Années", default='',related_name="annees_salaires")
    mois = models.CharField(max_length=250, choices=Mois, default=1, verbose_name="Mois")
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, verbose_name="Enseignants", default='',related_name="enseignant")
    salaire = models.IntegerField(verbose_name="Salaire (GNF)")
    date = models.CharField(max_length=250, verbose_name="Date du Paiement", default="01.01.2022")

    def get_absolute_url(self):
        return reverse('apps:salaires')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.enseignant)


class Charge(models.Model):
    annee = models.ForeignKey(Rentree, on_delete=models.CASCADE, null=True, verbose_name="Années", default='',related_name="annees_charges")
    mois = models.CharField(max_length=250, choices=Mois, default=1, verbose_name="Mois")
    commentaire = models.CharField(max_length=250,verbose_name="Commentaire")
    montant = models.IntegerField(verbose_name="Montant (GNF)")
    date = models.CharField(max_length=250, verbose_name="Date", default="01.01.2022")

    def get_absolute_url(self):
        return reverse('apps:charges')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.commentaire)
