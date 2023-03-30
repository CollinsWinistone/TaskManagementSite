# Generated by Django 4.1.7 on 2023-03-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_rename_client_sore_client_client_score'),
        ('projects', '0004_project_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.ManyToManyField(to='client.client'),
        ),
    ]