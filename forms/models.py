from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MyData(models.Model):
	firstname = models.CharField(max_length = 50)
	lastname = models.CharField(max_length = 50)
