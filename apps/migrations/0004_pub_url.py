# Generated by Django 3.2.7 on 2022-05-29 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_message_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='pub',
            name='url',
            field=models.CharField(default=1, max_length=250, verbose_name='Titre'),
            preserve_default=False,
        ),
    ]
