# Generated by Django 3.2.7 on 2022-10-05 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0027_alter_etablissement_annee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rentree',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='scolarite',
            name='annee',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.rentree', verbose_name='Année Scolaire'),
        ),
    ]
