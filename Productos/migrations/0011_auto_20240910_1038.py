# Generated by Django 3.2.25 on 2024-09-10 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores', '0001_initial'),
        ('Productos', '0010_alter_producto_proveedores'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='costo_producto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='producto',
            name='punto_reposicion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock_maximo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock_minimo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='existencias',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='producto',
            name='proveedores',
            field=models.ManyToManyField(through='Productos.Producto_Intermedia', to='Proveedores.Proveedor'),
        ),
    ]
