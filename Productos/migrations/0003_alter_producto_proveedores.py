# Generated by Django 5.0.7 on 2024-08-28 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0002_remove_producto_proveedores_producto_intermedia_and_more'),
        ('Proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='proveedores',
            field=models.ManyToManyField(through='Productos.Producto_Intermedia', to='Proveedores.proveedor'),
        ),
    ]
