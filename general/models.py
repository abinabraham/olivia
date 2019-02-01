# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ContactModel(models.Model):
	name = models.CharField(max_length=100,blank=True, null=True)
	email = models.EmailField()
	subject = models.CharField(max_length=100,blank=True, null=True)
	message=models.TextField(blank=True, null=True)
	created_on= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
