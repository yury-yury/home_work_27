from django.db import models


class Ads(models.Model):
    """
    The Ads class is an inheritor of the Model class from the models library. It is a data model contained
    in the ads database table. Contains a description of the types and constraints of the model fields.
    """
    STATUS = [("TRUE", "Опубликовано"),
              ("FALSE", "Не опубликовано")]
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=200)
    is_published = models.CharField(max_length=5, choices=STATUS, default="FALSE")


class Category(models.Model):
    """
    The Category class is an inheritor of the Model class from the models library. It is a data model contained
    in the category table of the database. Contains a description of the types and constraints of the model fields.
    """
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50)
