# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# from sweet.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Category, Order
from .forms import VendorSignUpForm, BrandProfileForm

# Create your views here.

def index(request):
	categories = Category.objects.all()
	return render(request, 'index.html', {'categories':categories})

# def shirt_order(request):
# 	if request.method == 'POST':
# 		shirtform = CreateOrderForm(data=request.POST)

# 		if shirtform.is_valid():
# 			shirt = shirtform.save()
# 			shirt.save()

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

def register_vendor(request):
	registered = False

	if request.method == 'POST':
		vendorform = VendorSignUpForm(data=request.POST)

		if vendorform.is_valid():
			vendor = vendorform.save()
			#  Hashing password with set_password method, update user object once hashed
			vendor.set_password(vendor.password)
			vendor.is_active = False
			vendor.is_staff = True
			vendor.save()

			registered = True
		else:
			print(vendorform.errors)
	else:
		vendorform = VendorSignUpForm()

	return render(request, 'sweet/vendor_register.html', {'vendorform':vendorform, 'registered':registered})

# def register_vendor_ose(request):
# 	if request.user.is_authenticated:
# 		return HttpResponseRedirect("/")
# 	if request.method == 'POST':
# 		form = VendorSignUpForm(request.POST)
# 		form2 = BrandProfileForm(request.POST)
# 		if form.is_valid() and form2.is_valid():
# 			user = form.save(commit=False)
# 			user.username = user.username.lower()
# 			user.is_active = False
# 			user.is_staff = True
# 			user.save()
# 			user.profile.phonenumber = number
# 			user.save()

# 			# send_sms("Juggernut", number, "Account Confirmation Message. Thank you for signing to Juggernut. Your presence is highly appreciated")

# 			'''
# 			current_site = get_current_site(request)
# 			subject = "Activate your Juggernut Account"
# 			message = render_to_string('registration/activation_email.html', {'user':user, 'domain':current_site.domain, 'uid':urlsafe_base64_encode(force_bytes(user.pk)), 'token':account_activation_token.make_token(user),})
# 			user.email_user(subject, message)
# 			return redirect('account_activation_sent')

# 			'''
# 	else:
# 		form = VendorSignUpForm()
# 		form2 = BrandProfileForm()
# 	return render(request, 'registration/vendor_registration_form.html', {'form':form, 'form2':form2})

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