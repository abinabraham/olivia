# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from phonenumber_fielsd.modelfields import PhoneNumberField

# Create your models here.

class ContactModel(models.Model):
	name = models.CharField(max_length=100,blank=True, null=True)
	email = models.EmailField()
	subject = models.CharField(max_length=100,blank=True, null=True)
	message=models.TextField(blank=True, null=True)
	created_on= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class ContactUsModel(models.Model):

	SUBJECT_CHOICES = (
        ('I Would Like To Discuss', 'I Would Like To Discuss'),
        ('I Would Like To Know About', 'I Would Like To Know About'),
        ('I Would Like To Suggest', 'I Would Like To Suggest'),
    )
	name = models.CharField(max_length=100,blank=True, null=True)
	email = models.EmailField()
	mob_no = models.CharField(max_length=12,null=False, blank=False)
	subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
	created_on= models.DateTimeField(auto_now=True)
