# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.

def index(request):
	categories = Category.objects.all()
	return render(request, 'index.html', {'categories':categories})

def vendor_index(request):
	return render(request, 'vendor_index.html', {})
