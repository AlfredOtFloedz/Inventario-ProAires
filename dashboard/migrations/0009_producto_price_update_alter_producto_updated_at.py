# Generated by Django 4.2.7 on 2023-11-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_producto_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='price_update',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
