# Generated by Django 3.2.7 on 2022-11-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0036_salaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='salaire',
            name='mois',
            field=models.CharField(choices=[('Janvier', 'Janvier'), ('Fevrier', 'Fevrier'), ('Mars', 'Mars'), ('Avril', 'Avril'), ('Mai', 'Mai'), ('Juin', 'Juin'), ('Juillet', 'Juillet')], default=1, max_length=250, verbose_name='Mois'),
        ),
    ]
