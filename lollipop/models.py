# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.template.defaultfilters import Slugify
# from django.db import models

# # Create your models here.

# class Lollipop_Salesman(models.Model):
# 	user = models.OneToOneField(User)
# 	profile_picture = models.ImageField(upload_to='profile_images', blank=True)
# 	portfolio = models.TextField()
# 	likes = models.IntegerField(default=0)
# 	email = models.EmailField(max_length=50, default='abc@gmail.com', unique=True)

# class Category(models.Model):
# 	name = models.CharField(max_length=50, unique=True, db_index=True)
# 	slug = models.SlugField(max_length=50, unique=True, db_index=True)

# 	class Meta:
# 		ordering = ('name',)
# 		verbose_name_plural = "Categories"

# 	# REMEMBER TO ADD GET_ABSOLUTE_URL

# 	def __str__(self):
# 		return self.name

# class Product(models.Model):
# 	name = models.CharField(max_length=50, unique=True)
# 	category = models.ForeignKey(Category)
# 	quantity = models.IntegerField(default=0)