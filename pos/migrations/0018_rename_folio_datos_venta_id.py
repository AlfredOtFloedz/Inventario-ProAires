# Generated by Django 4.2.7 on 2023-12-07 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0017_alter_datos_venta_tipo_factura'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datos_venta',
            old_name='folio',
            new_name='id',
        ),
    ]
