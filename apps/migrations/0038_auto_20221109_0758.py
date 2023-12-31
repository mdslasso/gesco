# Generated by Django 3.2.7 on 2022-11-09 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0037_salaire_mois'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaire',
            name='annee',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='annees_salaires', to='apps.rentree', verbose_name='Années'),
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.CharField(choices=[('Janvier', 'Janvier'), ('Fevrier', 'Fevrier'), ('Mars', 'Mars'), ('Avril', 'Avril'), ('Mai', 'Mai'), ('Juin', 'Juin'), ('Juillet', 'Juillet')], default=1, max_length=250, verbose_name='Mois')),
                ('montant', models.IntegerField(verbose_name='Montant (GNF)')),
                ('date', models.CharField(default='01.01.2022', max_length=250, verbose_name='Date du Payement')),
                ('annee', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='annees_charges', to='apps.rentree', verbose_name='Années')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
