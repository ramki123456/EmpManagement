from __future__ import unicode_literals

from django.db import models
from Task.settings import BASE_DIR
# Create your models here.

class Employee(models.Model):
    employee_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    photo =  models.ImageField(upload_to='{0}\MyApp\static\images'.format(BASE_DIR), max_length=100)




    def __unicode__(self):
    	return self.name