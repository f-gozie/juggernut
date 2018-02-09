# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# from sweet.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Category, Product

# Create your views here.

def index(request):
	categories = Category.objects.all()
	return render(request, 'index.html', {'categories':categories})

def register(request):
	registered = False

	if request.method == 'POST':
		userform = UserForm(data=request.POST)

		if userform.is_valid():
			user = userform.save()
			# Hashing password with set_password method, update user object once hashed
			user.set_password(user.password)
			user.save()

			registered = True
		else:
			print(userform.errors)
	else:
		userform = UserForm()

	return render(request, 'sweet/register.html', {'userform':userform, 'registered':registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your account has been disabled")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'sweet/login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))