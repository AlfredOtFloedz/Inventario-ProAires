# Generated by Django 4.2.7 on 2023-11-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_alter_producto_quantity_alter_producto_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, default=10000.0, max_digits=20),
        ),
    ]