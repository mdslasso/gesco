# Generated by Django 3.2.7 on 2022-11-18 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0045_auto_20221118_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='matricule',
            field=models.FloatField(null=True, unique=True, verbose_name='Matricule'),
        ),
    ]