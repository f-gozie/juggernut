from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
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