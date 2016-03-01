from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=16)
    age = models.DecimalField(decimal_places=0, max_digits=2)
    bill_in_day = models.DecimalField(decimal_places=1, max_digits=4)