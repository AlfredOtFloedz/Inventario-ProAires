# Generated by Django 4.2.7 on 2023-11-28 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_alter_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='RFC',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]