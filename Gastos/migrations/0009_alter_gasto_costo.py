# Generated by Django 4.2.13 on 2024-10-25 16:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gastos', '0008_auto_20241002_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='costo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]