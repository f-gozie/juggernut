from django import forms
from django.contrib.auth import authenticate

def file_size(value):
	limit = 1.5 * 1024 * 1024
	if value.size > limit:
		raise forms.ValidationError("File size too large. Must not exceed 1.5 MiB.")
		