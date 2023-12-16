# Generated by Django 4.2.7 on 2023-12-16 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0022_alter_pos_equipo_equipo_alter_pos_equipo_precio_gral'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datos_venta',
            options={'verbose_name_plural': 'Orden de compra'},
        ),
        migrations.AlterModelOptions(
            name='pos_equipo',
            options={'verbose_name_plural': 'Adquisición de Equipo'},
        ),
        migrations.AddField(
            model_name='pos_equipo',
            name='precio_tec',
            field=models.PositiveIntegerField(default=10000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pos_equipo',
            name='equipo',
            field=models.CharField(choices=[('INVERTER 17 - 1 ton 110V', 'INVERTER 17 - 1 ton 110V'), ('INVERTER 17 - 1 ton 220V', 'INVERTER 17 - 1 ton 220V'), ('INVERTER 17 - 1.5 ton 220V', 'INVERTER 17 - 1.5 ton 220V'), ('INVERTER 17 - 2 ton 220V', 'INVERTER 17 - 2 ton 220V'), ('INVERTER 17 - 3 ton 220V', 'INVERTER 17 - 3 ton 220V'), ('INVERTER X - 1 ton 110V', 'INVERTER X - 1 ton 110V'), ('INVERTER X - 1 ton 220V', 'INVERTER X - 1 ton 220V'), ('INVERTER X - 1.5 ton 220V', 'INVERTER X - 1.5 ton 220V'), ('INVERTER X - 2 ton 220V', 'INVERTER X - 2 ton 220V'), ('LIFE 12 - 1 ton 110V', 'LIFE 12 - 1 ton 110V'), ('LIFE 12 - 1 ton 220V', 'LIFE 12 - 1 ton 220V'), ('LIFE 12 - 1.5 ton 220V', 'LIFE 12 - 1.5 ton 220V'), ('LIFE 12 - 2 ton 220V', 'LIFE 12 - 2 ton 220V'), ('LIFE 12 PLUS - 1 ton 110V', 'LIFE 12 PLUS - 1 ton 110V'), ('LIFE 12 PLUS - 1 ton 220V', 'LIFE 12 PLUS - 1 ton 220V'), ('LIFE 12 PLUS - 1.5 ton 220V', 'LIFE 12 PLUS - 1.5 ton 220V'), ('LIFE 12 PLUS - 2 ton 220V', 'LIFE 12 PLUS - 2 ton 220V'), ('MAGNUM 22 INV - 1 ton 110V', 'MAGNUM 22 INV - 1 ton 110V'), ('MAGNUM 22 INV - 1 ton 220V', 'MAGNUM 22 INV - 1 ton 220V'), ('MAGNUM 22 INV - 1.5 ton 220V', 'MAGNUM 22 INV - 1.5 ton 220V'), ('MAGNUM 22 INV - 2 ton 220V', 'MAGNUM 22 INV - 2 ton 220V'), ('NEX - 1 ton 110V', 'NEX - 1 ton 110V'), ('NEX - 1 ton 220V', 'NEX - 1 ton 220V'), ('NEX - 1.5 ton 220V', 'NEX - 1.5 ton 220V'), ('NEX - 2 ton 220V', 'NEX - 2 ton 220V'), ('V32 INVERTER - 1 ton 110V', 'V32 INVERTER - 1 ton 110V'), ('V32 INVERTER - 1 ton 220V', 'V32 INVERTER - 1 ton 220V'), ('V32 INVERTER - 1.5 ton 220V', 'V32 INVERTER - 1.5 ton 220V'), ('V32 INVERTER - 2 ton 220V', 'V32 INVERTER - 2 ton 220V'), ('XLIFE - 1 ton 110V', 'XLIFE - 1 ton 110V'), ('XLIFE - 1 ton 220V', 'XLIFE - 1 ton 220V'), ('XLIFE - 1.5 ton 220V', 'XLIFE - 1.5 ton 220V'), ('XLIFE - 2 ton 220V', 'XLIFE - 2 ton 220V'), ('X32 INVERTER - 1 ton 110V', 'X32 INVERTER - 1 ton 110V'), ('X32 INVERTER - 1 ton 220V', 'X32 INVERTER - 1 ton 220V'), ('X32 INVERTER - 1.5 ton 220V', 'X32 INVERTER - 1.5 ton 220V'), ('X32 INVERTER - 2 ton 220V', 'X32 INVERTER - 2 ton 220V'), ('X-ONE - 1 ton 110V', 'X-ONE - 1 ton 110V')], max_length=100),
        ),
    ]
