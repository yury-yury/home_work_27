# Generated by Django 4.1.7 on 2023-03-14 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0008_alter_ads_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='price',
            field=models.IntegerField(),
        ),
    ]