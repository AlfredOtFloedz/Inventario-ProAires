# Generated by Django 4.2.7 on 2023-12-11 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0020_alter_datos_venta_forma_pago_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pos_equipo',
            name='descuento',
        ),
        migrations.RemoveField(
            model_name='pos_equipo',
            name='precio_u',
        ),
        migrations.AddField(
            model_name='pos_equipo',
            name='precio_gral',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pos_equipo',
            name='equipo',
            field=models.CharField(choices=[('INVERTER 17 - 1 ton 110V', 'INVERTER 17 - 1 ton 110V'), ('INVERTER 17 - 1 ton 220V', 'INVERTER 17 - 1 ton 220V'), ('INVERTER 17 - 1.5 ton 220V', 'INVERTER 17 - 1.5 ton 220V'), ('INVERTER 17 - 2 ton 220V', 'INVERTER 17 - 2 ton 220V'), ('INVERTER 17 - 3 ton 220V', 'INVERTER 17 - 2 ton 220V'), ('INVERTER X - 1 ton 110V', 'INVERTER X - 1 ton 110V'), ('INVERTER X - 1 ton 220V', 'INVERTER X - 1 ton 220V'), ('INVERTER X - 1.5 ton 220V', 'INVERTER X - 1.5 ton 220V'), ('INVERTER X - 2 ton 220V', 'INVERTER X - 2 ton 220V'), ('LIFE 12 - 1 ton 110V', 'LIFE 12 - 1 ton 110V'), ('LIFE 12 - 1 ton 220V', 'LIFE 12 - 1 ton 220V'), ('LIFE 12 - 1.5 ton 110V', 'LIFE 12 - 1.5 ton 110V'), ('LIFE 12 - 2 ton 110V', 'LIFE 12 - 2 ton 110V'), ('LIFE 12 PLUS - 1 ton 110V', 'LIFE 12 PLUS - 1 ton 110V'), ('LIFE 12 PLUS - 1 ton 220V', 'LIFE 12 PLUS - 1 ton 220V'), ('LIFE 12 PLUS - 1.5 ton 110V', 'LIFE 12 PLUS - 1.5 ton 110V'), ('LIFE 12 PLUS - 2 ton 110V', 'LIFE 12 PLUS - 2 ton 110V'), ('MAGNUM 18 INV - 1 ton 110V', 'MAGNUM 18 INV - 1 ton 110V'), ('MAGNUM 21 PLATINUM - 1 ton 110V', 'MAGNUM 21 PLATINUM - 1 ton 110V'), ('MAGNUM 21 PLATINUM - 1 ton 220V', 'MAGNUM 21 PLATINUM - 1 ton 220V'), ('MAGNUM 22 INV - 1 ton 110V', 'MAGNUM 22 INV - 1 ton 110V'), ('MAGNUM 22 INV - 1 ton 220V', 'MAGNUM 22 INV - 1 ton 220V'), ('MAGNUM 22 INV - 1.5 ton 110V', 'MAGNUM 22 INV - 1.5 ton 110V'), ('MAGNUM 22 INV - 2 ton 110V', 'MAGNUM 22 INV - 2 ton 110V'), ('NEX - 1 ton 110V', 'NEX - 1 ton 110V'), ('NEX - 1 ton 220V', 'NEX - 1 ton 220V'), ('NEX - 1.5 ton 110V', 'NEX - 1.5 ton 110V'), ('NEX - 2 ton 110V', 'NEX - 2 ton 110V'), ('V32 INVERTER - 1 ton 110V', 'V32 INVERTER - 1 ton 110V'), ('V32 INVERTER - 1 ton 220V', 'V32 INVERTER - 1 ton 220V'), ('V32 INVERTER - 1.5 ton 110V', 'V32 INVERTER - 1.5 ton 110V'), ('V32 INVERTER - 2 ton 110V', 'V32 INVERTER - 2 ton 110V'), ('XLIFE - 1 ton 110V', 'XLIFE - 1 ton 110V'), ('XLIFE - 1 ton 220V', 'XLIFE - 1 ton 220V'), ('XLIFE - 1.5 ton 110V', 'XLIFE - 1.5 ton 110V'), ('XLIFE - 2 ton 110V', 'XLIFE - 2 ton 110V'), ('X32 INVERTER - 1 ton 110V', 'X32 INVERTER - 1 ton 110V'), ('X32 INVERTER - 1 ton 220V', 'X32 INVERTER - 1 ton 220V'), ('X32 INVERTER - 1.5 ton 110V', 'X32 INVERTER - 1.5 ton 110V'), ('X32 INVERTER - 2 ton 110V', 'X32 INVERTER - 2 ton 110V'), ('X-ONE - 1 ton 110V', 'X-ONE - 1 ton 110V')], max_length=100),
        ),
    ]
