from __future__ import unicode_literals

from django.db import models

# Create your models here.
class newdb(models.Model):
    name=models.CharField(max_length=15)
    password=models.IntegerField(max_length=10)
    def __str__(self):
        return self.name
