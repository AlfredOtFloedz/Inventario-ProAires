# Generated by Django 4.2.7 on 2023-11-22 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_remove_producto_modelo_producto_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='type',
        ),
    ]
