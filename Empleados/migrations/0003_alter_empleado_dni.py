# Generated by Django 4.2.13 on 2024-10-25 16:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0002_alter_empleado_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='dni',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(8)], verbose_name='DNI'),
        ),
    ]
