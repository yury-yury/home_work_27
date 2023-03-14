from django.db import models


class Ads(models.Model):
    STATUS = [("TRUE", "Опубликовано"),
              ("FALSE", "Не опубликовано")]
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.BigIntegerField()
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=200)
    is_published = models.CharField(max_length=5, choices=STATUS, default="FALSE")


class Category(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50)
