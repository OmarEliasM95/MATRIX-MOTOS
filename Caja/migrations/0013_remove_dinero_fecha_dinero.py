# Generated by Django 3.2.25 on 2024-10-09 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Caja', '0012_auto_20241009_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dinero',
            name='fecha_dinero',
        ),
    ]
