# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# Create your models here.

class Operator(models.Model):
	user = models.OneToOneField(User)
	domain = models.URLField()
	profile_picture = models.ImageField(upload_to="profile_images", blank=True)
	description = models.TextField()
	occupation = models.CharField(max_length=2, choices=(('D', 'DryCleaner'), ('T', 'Tailor')))
	gender = models.CharField(max_length=2,choices=(('M','Male'),('F','Female')))
	def save(self, *args, **kwargs):
		self.is_staff = True
		super(Operator, self).save(*args, **kwargs)

	def __str__(self):
		return self.user.username

	def __unicode__(self):
		return self.user.username

# class Tailor(models.Model):
# 	user = models.OneToOneField(User)
# 	domain = models.URLField()
# 	profile_picture = models.ImageField(upload_to="profile_images", blank=True)
# 	description = models.TextField()

# 	def save(self,*args,**kwargs):
#         self.is_staff = True
#         super(Retailer, self).save(*args,**kwargs)

	def __str__(self):
		return self.user.username

	def __unicode__(self):
		return self.user.username

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

class Order(models.Model):
	name = models.CharField(max_length=20)
	slug = models.SlugField(db_index=True, max_length=50)
	category = models.ForeignKey(Category)
	description = models.TextField()
	gender = models.CharField(max_length=2,choices=(('M','Male'),('F','Female')))
	quantity = models.PositiveIntegerField(default=0)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=200, null=False)
	operator_id = models.ForeignKey(Operator)
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