from django import forms
from django.contrib.auth.models import User
from .models import Profile, Image
from django.contrib.auth import authenticate
from sweet.forms import file_size

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password')

# Clean email method is commented so as to allow for proper testing with one email
'''
	def clean_email(self):
		email = self.cleaned_data.get('email')
    	if email and User.objects.filter(email=email).exists():
    		raise forms.ValidationError('Email address already in use. Must be unique')

    	return email
'''

# CHOICES = [('M', 'Male'), ('F', 'Female')]
# class CreateOrderForm(forms.ModelForm):
# 	description = forms.CharField(label="Special Instructions", widget=forms.TextInput(attrs={'style':"font-weight:bold;font-size:16px; font-family:'Calibri"}))
# 	gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

# 	class Meta:
# 		model = Product
# 		exclude = ('transport_cost', 'created', 'updated', 'price', 'operator_id', )

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', widget=forms.TextInput(attrs={ 'style':"font-weight:bold;font-size:16px; font-family:'Calibri"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={ 'style':"font-weight:bold;font-size:16px; font-family:'Calibri"}))

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		username = username.lower()
		password = self.cleaned_data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Username and Password do not match!")

		return super(LoginForm, self).clean(*args, **kwargs)
	class Meta:
		model = User
		fields = ('username', 'password',)


class VendorSignUpForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name of brand','style': "font-weight:bold; font-family:'Calibri';",'autofocus':'autofocus' }), max_length=15)
	phonenumber = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Phone Number','style': "font-weight:bold; font-family:'Calibri';"}), max_length=11,required=False)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Input Password','style': "font-weight:bold; font-family:'Calibri';"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Input Password Again','style': "font-weight:bold; font-family:'Calibri';"}))

	class Meta:
		model = User
		fields = ('email','username','phonenumber','password1','password2')

class BrandProfileForm(forms.ModelForm):
	phonenumber = forms.CharField(required=False)
	profilepicture = forms.ImageField(required=False, validators=[file_size])

	class Meta:
		model = Profile
		fields = ('profilepicture', 'phonenumber')