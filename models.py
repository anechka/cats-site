# coding: utf-8
from django.db import models
from django.contrib import admin

class Cat(models.Model):
    name = models.CharField(max_length=16)
    age = models.DecimalField(decimal_places=1, max_digits=3)
    bill_in_day = models.DecimalField(decimal_places=1, max_digits=4)


print admin.site.register(Cat)