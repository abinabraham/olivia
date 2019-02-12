# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView,CreateView, View
from django.shortcuts import render
from general.models import ContactUsModel
from django.shortcuts import redirect
from django.contrib import messages

class HomeView(View):
    template_name = 'index.html'


    def get(self, request, *args, **kwargs):
        context_dict = {}
        return render(request,"index.html",context_dict)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('username')
        email = request.POST.get('email')
        subjt = request.POST.get('subject')
        mob_no = request.POST.get('phone')
        if subjt=='0' and subjt=='1' :
            subjt = 'I Would Like To Discuss'
        elif subjt=='2':
            subjt = 'I Would Like To Know About'
        else:
            subjt = 'I Would Like To Suggest'
        try:
            contct_obj = ContactUsModel.objects.create(name=name,email=email,subject=subjt,mob_no=mob_no)
            messages.success(request, 'Thank you!. Your request has been successfully sent. We will contact you soon.') 
        except Exception as e:
            print "+++=e",e
            messages.error(request, 'Oops. Something went wrong. Try again!.',e) 

        
        return redirect("/#contact")