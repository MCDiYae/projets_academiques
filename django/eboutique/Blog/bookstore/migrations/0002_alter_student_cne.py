# Generated by Django 5.0.1 on 2024-01-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='CNE',
            field=models.IntegerField(),
        ),
    ]
