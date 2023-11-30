# Generated by Django 4.2.7 on 2023-11-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_remove_precios_category_remove_precios_precio_compra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='category',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='producto',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='producto',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
