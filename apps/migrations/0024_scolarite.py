# Generated by Django 3.2.7 on 2022-10-02 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0023_inscription_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scolarite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payement', models.IntegerField(verbose_name='Payement (GNF)')),
                ('date', models.CharField(default='01.01.2022', max_length=250, verbose_name='Date du Payement')),
                ('classe', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.classe', verbose_name='Classes')),
                ('etudiant', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.etudiant', verbose_name='Étudiants')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
