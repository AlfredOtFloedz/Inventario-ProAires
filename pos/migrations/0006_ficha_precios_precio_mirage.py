# Generated by Django 4.2.7 on 2023-12-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0005_ficha_precios_pos_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha_precios',
            name='precio_mirage',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
