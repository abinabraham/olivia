# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from models import ContactUsModel

# Create your views here.
class NewContact(View): 
	'''view for saving contact details'''

	def post(self,request):
		name = request.POST.get('name')
		email = request.POST.get('email')
		subjt = request.POST.get('subject')
		mob_no = request.POST.get('mob_no')
		print("ttttttttttttt",subjt,type(subjt))
		if subjt=='0' and subjt=='1' :
			print("first>...................")
			subjt = 'I Would Like To Discuss'
		elif subjt=='2':
			print("sssssssssssssssssssssss")
			subjt = 'I Would Like To Know About'
		else:
			print("ttttttttttttttt")
			subjt = 'I Would Like To Suggest'
		# print("in viewwwwwwwwwwwwwwwwwwwww",name,email,subjt,msg)
		contct_obj = ContactUsModel.objects.create(name=name,email=email,subject=subjt,mob_no=mob_no)
		return HttpResponse(json.dumps('success'), content_type='json')


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
@method_decorator(login_required, name='dispatch')
class OliviaDashboard(View):
	template_name = 'dashboard.html'
	'''view for showing dashboard '''

	def get(self,request):
		print("get")
		contact_obj = ContactUsModel.objects.all()
		# context = {
		# 	'contacts':contact_obj
		# }
		return render(request,self.template_name,{'data':contact_obj})


	# def post(self,request):
	# 	print("post")
	# 	return render(request,self.template_name)