# Generated by Django 4.2.1 on 2023-06-16 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0002_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='foto',
            field=models.ImageField(null=True, upload_to='profesional'),
        ),
    ]
