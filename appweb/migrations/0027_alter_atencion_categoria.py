# Generated by Django 4.2.1 on 2023-07-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0026_alter_trabajaconnosotros_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='categoria',
            field=models.CharField(choices=[[0, 'Electronica'], [1, 'Cajas de Cambio'], [2, 'Suspensión y Frenos']], max_length=20),
        ),
    ]
