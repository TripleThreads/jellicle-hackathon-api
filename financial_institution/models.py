from django.db import models


class FinancialInstitution(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    region = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    account_id = models.IntegerField()
    user_id = models.IntegerField()
