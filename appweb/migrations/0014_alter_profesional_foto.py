# Generated by Django 4.2.1 on 2023-06-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0013_remove_profesional_contraseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='foto',
            field=models.ImageField(null=True, upload_to='Profesional'),
        ),
    ]