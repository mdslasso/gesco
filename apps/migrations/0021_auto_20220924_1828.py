# Generated by Django 3.2.7 on 2022-09-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0020_auto_20220923_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='filiation',
        ),
        migrations.AddField(
            model_name='etudiant',
            name='mere',
            field=models.CharField(default=2, max_length=250, verbose_name='Nom de la mère'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etudiant',
            name='pere',
            field=models.CharField(default=2, max_length=250, verbose_name='Nom du père '),
            preserve_default=False,
        ),
    ]
