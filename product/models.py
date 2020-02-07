from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
