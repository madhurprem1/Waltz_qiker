# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_code = models.CharField(max_length=50, unique=True)
    Department_Choices = (('D1','Engineering'),('D2','HR'),('D3','Operations'),('Waltzz','Waltzz'))
    score = models.IntegerField(max_length=None)
    date_created = models.DateField(auto_now_add=True)
    department = models.CharField(max_length=6, choices=Department_Choices, null=False)