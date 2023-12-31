# Generated by Django 3.2.7 on 2022-11-18 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0043_alter_enseignant_matricule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='matricule',
            field=models.PositiveIntegerField(unique=True, verbose_name='Matricule'),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='matricule',
            field=models.PositiveIntegerField(unique=True, verbose_name='Matricule'),
        ),
    ]
