# Generated by Django 4.1.7 on 2023-03-29 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='Client_sore',
            new_name='client_score',
        ),
    ]
