# Generated by Django 4.2.1 on 2023-06-27 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appweb', '0010_atencion_mecanico'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cargo',
        ),
        migrations.AddField(
            model_name='profesional',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
