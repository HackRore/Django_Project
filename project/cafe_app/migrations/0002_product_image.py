# Generated by Django 3.1.7 on 2025-04-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
