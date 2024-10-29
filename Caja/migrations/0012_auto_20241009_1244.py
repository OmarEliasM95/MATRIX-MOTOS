# Generated by Django 3.2.25 on 2024-10-09 15:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Caja', '0011_caja_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='fecha_apertura',
        ),
        migrations.RemoveField(
            model_name='caja',
            name='fecha_cierre',
        ),
        migrations.AlterField(
            model_name='dinero',
            name='fecha_dinero',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]