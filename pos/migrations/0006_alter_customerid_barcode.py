# Generated by Django 4.2.7 on 2023-11-28 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0005_customerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerid',
            name='barcode',
            field=models.ImageField(blank=True, upload_to='Profile_Images'),
        ),
    ]