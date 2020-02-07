from django.db import models


class Account(models.Model):
    current_amount = models.IntegerField()
