# Generated by Django 3.2.7 on 2022-05-26 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_message_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='numero',
            field=models.IntegerField(),
        ),
    ]
