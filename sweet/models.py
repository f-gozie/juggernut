# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from PIL import Image
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from io import BytesIO
from django.core.files.base import ContentFile
import requests
# Create your models here.

# class Operator(models.Model):
# 	user = models.OneToOneField(User)
# 	domain = models.URLField()
# 	profile_picture = models.ImageField(upload_to="profile_images", blank=True)
# 	description = models.TextField()
# 	occupation = models.CharField(max_length=2, choices=(('D', 'DryCleaner'), ('T', 'Tailor')))
# 	gender = models.CharField(max_length=2,choices=(('M','Male'),('F','Female')))
# 	def save(self, *args, **kwargs):
# 		self.is_staff = True
# 		super(Operator, self).save(*args, **kwargs)

# 	def __str__(self):
# 		return self.user.username

# 	def __unicode__(self):
# 		return self.user.username

class Category(models.Model):
	name = models.CharField(max_length=50, unique=True, db_index=True)
	slug = models.SlugField(max_length=50, unique=True, db_index=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = 'Categories'

	def get_absolute_url(self):
		return reverse('sweet:product_view_by_category', args=[self.slug])

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name


def send_sms(my_sender, receiver, my_message):
	api_username = "juggernut"
	api_password = "juggernut"
	parameters = {"username":api_username, "password":api_password, "destination":receiver, "message":my_message, "sender":my_sender}
	response = requests.post("http://www.supertextng.com/api.php?", data=parameters)
	return response



# class SendTestSMS(models.Model):
# 	to_number = models.CharField(max_length=20)
# 	from_number = models.CharField(max_length=20)
# 	sms_sid = models.CharField(max_length=50, default='', blank=True)
# 	account_sid = models.CharField(max_length=50, default="", blank=True)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	sent_at = models.DateTimeField(auto_now_add=True)
# 	delivered_at = models.DateTimeField(null=True, blank=True)
# 	status = models.CharField(max_length=20, default="", blank=True)

