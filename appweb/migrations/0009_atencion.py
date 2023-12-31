# Generated by Django 4.2.1 on 2023-06-26 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0008_rename_apellido_paterno_contacto_apellido_paterno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(null=True, upload_to='')),
                ('categoria', models.IntegerField(choices=[[0, 'Electronica'], [1, 'Cajas de Cambio'], [2, 'Suspensión y Frenos']])),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
