# Generated by Django 4.2.1 on 2023-05-27 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidoPaterno', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=8)),
                ('foto', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]
