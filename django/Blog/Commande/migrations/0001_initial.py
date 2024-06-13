# Generated by Django 5.0 on 2024-01-05 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0001_initial'),
        ('Livre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreation', models.DateField(auto_now_add=True)),
                ('qte', models.IntegerField(null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Client.client')),
                ('livre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Livre.livre')),
            ],
        ),
    ]
