# Generated by Django 4.2.1 on 2023-06-16 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0006_alter_contacto_tipos_contacto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='apellidoPaterno',
            new_name='apellido_paterno',
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='tipos_contacto',
            new_name='motivo',
        ),
    ]
