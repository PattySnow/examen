# Generated by Django 4.2.1 on 2023-06-16 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0004_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tipos_contacto',
            field=models.IntegerField(choices=[[0, 'sugerencia'], [1, 'Reclamo'], [2, 'Felicitaciones']]),
        ),
    ]