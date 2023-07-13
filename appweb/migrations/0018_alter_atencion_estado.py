# Generated by Django 4.2.1 on 2023-06-29 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0017_atencion_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='estado',
            field=models.IntegerField(choices=[[0, 'En Espera'], [1, 'Aprobada'], [2, 'Rechazada']], default=0, null=True),
        ),
    ]
