from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
# from sweet.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import VendorSignUpForm, BrandProfileForm, LoginForm
from django.core.mail import EmailMessage, EmailMultiAlternatives
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
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

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.is_email_verified = True
		user.save()
		login(request, user)
		if user.is_staff:
			return redirect('sweet:vendor_index')
		else:
			return redirect('sweet:index')
		# return HttpResponse('Thank you for your email confirmation. Now you can login to your account.')
	else:
		return HttpResponse("Invalid activation link")

def email_confirm(request):
	return render(request, "email_confirm.html", {})

def register_vendor(request):
	registered = False

	if request.method == 'POST':
		vendorform = VendorSignUpForm(data=request.POST)

		if vendorform.is_valid():
			vendor = vendorform.save(commit=False)
			#  Hashing password with set_password method, update user object once hashed
			vendor.set_password(vendor.password)
			vendor.is_active = False
			vendor.is_staff = True
			vendor.save()

			# current_site = get_current_site(request)
			text_content = "Account Activation Email"
			mail_subject = "Activate you Juggernut account"
			template_name = 'account_activate.html'
			from_email = vendorform.cleaned_data.get('email')
			recipients = [vendor.email]
			kwargs = {
				"uidb64":urlsafe_base64_encode(force_bytes(vendor.pk)).decode(),
				"token":account_activation_token.make_token(vendor)
			}
			activation_url = reverse("myregistration:activate", kwargs=kwargs)

			activation_url = "{0}://{1}{2}".format(request.scheme, request.get_host(), activation_url)

			context = {
				'vendor':vendor,
				'activation_url':activation_url
			}
			html_content = render_to_string(template_name, context)
			email = EmailMultiAlternatives(mail_subject, text_content, from_email, recipients)
			email.attach_alternative(html_content, "text/html")
			email.send()
			return redirect("myregistration:email_confirm")
			registered = True
		else:
			print(vendorform.errors)
	else:
		vendorform = VendorSignUpForm()

	return render(request, 'register_vendor.html', {'vendorform':vendorform, 'registered':registered})

def vendor_login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect("/")
	form = LoginForm()
	errors = None
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			username = username.lower()
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			login(request, user)
			if user.is_staff:
				return redirect('sweet:vendor_index')
			else:
				return redirect('sweet:index')
		else:
			errors = "Invalid Username or Password"
	return render(request, 'vendor_login.html', {'form':form, 'errors':errors})

@login_required
def vendor_logout(request):
	logout(request)
	return redirect('vendor_login')

def password_change(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash() # This is vital so as not to log user out during current session
			message.success(request, "Your password was successfully updated")
			return redirect('sweet:index')
		else:
			messages.error(request, "Please take a look at the completed form and correct all errors")
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'password_change.html', {'form':form})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('sweet:index'))
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
	return HttpResponseRedirect(reverse('sweet:index'))