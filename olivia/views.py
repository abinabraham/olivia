# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView,CreateView




# Create your views here.
class HomeView(TemplateView):
	template_name = 'index.html'