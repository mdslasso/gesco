# Generated by Django 3.2.7 on 2022-10-04 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0025_inscription_statut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='statut',
        ),
    ]
