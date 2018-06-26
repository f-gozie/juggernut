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

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	domain = models.URLField()
	# Set profile_picture required to true, people don't trust anonymity.
	profile_picture = models.ImageField(upload_to='profile_images', blank=False)
	phonenumber = models.CharField(default="0", max_length=11)
	email_confirmed = models.BooleanField(default=False)
	visits = models.IntegerField(default=0)
	occupation = models.CharField(max_length=2, choices=(('D', 'DryCleaner'), ('T', 'Tailor')))
	gender = models.CharField(max_length=2, choices=(('M','Male'),('F', 'Female')))
	description = models.CharField(max_length=2500, blank=True, default='description')

	def save(self, *args, **kwargs):
		if self.profile_picture and self.profile_picture.size > 512000:
			pil_image_obj = Image.open(self.profile_picture)

			new_image_io = BytesIO()
			pil_image_obj.save(new_image_io, format='JPEG', quality=70)

			temporary_name = self.profile_picture.name
			self.profile_picture.delete(save=False)

			self.profile_picture.save(temporary_name, content=ContentFile(new_image_io.getvalue()), save=False)

		super(Profile, self).save(*args, **kwargs)

	def __str__(self):
		return self.user.username

	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def update_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)
		instance.profile.save()

class Image(models.Model):
	image = models.ImageField(verbose_name='images', upload_to='profile_images', null=True, blank=True)
	vendor = models.ForeignKey(User)

	def save(self, *args, **kwargs):
		if self.image and self.image.size > 512000:
			pil_image_obj = Image.open(self.image)

			new_image_io = BytesIO()
			pil_image_obj.save(new_image_io, format='JPEG', quality=70)

			temporary_name = self.image.name
			self.image.delete(save=False)

			self.image.save(temporary_name, content=ContentFile(new_image_io.getvalue()), save=False)

		super(Image, self).save(*args, **kwargs)

	def __str__(self):
		return self.vendor.username

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

class Order(models.Model):
	name = models.CharField(max_length=20)
	slug = models.SlugField(db_index=True, max_length=50)
	category = models.ForeignKey(Category)
	description = models.TextField()
	gender = models.CharField(max_length=2,choices=(('M','Male'),('F','Female')))
	quantity = models.PositiveIntegerField(default=0)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=200, null=False)
	operator_id = models.ForeignKey(Profile)
	transport_cost= models.IntegerField(default=200)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name