# Generated by Django 4.1.7 on 2023-03-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ads_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='price',
            field=models.BigIntegerField(null=True),
        ),
    ]
