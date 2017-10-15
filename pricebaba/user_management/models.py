from __future__ import unicode_literals
from django.db import models


class Pricebaba_Users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	mobile = models.CharField(max_length=15)
	age = models.IntegerField()
	dob = models.CharField(max_length=100)
	location = models.CharField(max_length=255)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
	created_on = models.DateTimeField(auto_now=False,auto_now_add=True)


