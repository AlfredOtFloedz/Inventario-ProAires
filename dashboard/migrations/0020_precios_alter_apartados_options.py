# Generated by Django 4.2.7 on 2023-11-29 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_apartados'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_compra', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(default=None, max_length=100)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='apartados',
            options={'verbose_name_plural': 'Apartados'},
        ),
    ]
