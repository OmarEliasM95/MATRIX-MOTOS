# Generated by Django 3.2.25 on 2024-09-26 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Compras', '0005_alter_compra_metodo_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]