# Generated by Django 4.2.7 on 2023-12-07 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0016_alter_datos_venta_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_venta',
            name='tipo_factura',
            field=models.CharField(choices=[('Cliente', 'Cliente'), ('Empresa', 'Empresa'), ('Público en General', 'Publico en General')], max_length=100),
        ),
    ]
