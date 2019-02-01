# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from models import ContactModel

# Create your views here.
class NewContact(View): 
	'''view for saving contact details'''

	def post(self,request):
		name = request.POST.get('name')
		email = request.POST.get('email')
		subjt = request.POST.get('subject')
		msg = request.POST.get('message')
		# print("in viewwwwwwwwwwwwwwwwwwwww",name,email,subjt,msg)
		contct_obj = ContactModel.objects.create(name=name,email=email,subject=subjt,message=msg)
		return HttpResponse(json.dumps('success'), content_type='json')

class OliviaDashboard(View):
	template_name = 'dashboard.html'
	'''view for showing dashboard '''

	def get(self,request):
		print("get")
		return render(request,self.template_name)


	def post(self,request):
		print("post")
		return render(request,self.template_name)