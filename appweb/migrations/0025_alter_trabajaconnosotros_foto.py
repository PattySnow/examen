# Generated by Django 4.2.1 on 2023-07-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0024_alter_trabajaconnosotros_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajaconnosotros',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
