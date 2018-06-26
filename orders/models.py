# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.template.defaultfilters import slugify
# from django.db import models
# from sweet.models import Product

#  # Create your models here.

# CURRENT_STATUS = (
# 		("Started", "Started"),
# 		("Processing", "Processing"),
# 		("Pending", "Pending"),
# 		("Shipping", "Shipping"),
# 		("Delivered", "Delivered"),
# 	)

# class Order(models.Model):
# 	first_name = models.CharField(max_length=20)
# 	last_name = models.CharField(max_length=20)
# 	phonenumber = models.CharField(max_length=11)
# 	email_address = models.EmailField()
# 	address = models.CharField(max_length=100)
# 	city = models.Charfield(max_length=100)
# 	operator_id = models.ForeignKey(Profile)
# 	status = models.CharField(max_length=100, choices=CURRENT_STATUS, default='Started')
# 	slug = models.SlugField(db_index=True, max_length=50)
# 	category = models.ForeignKey(Category)
# 	description = models.TextField()
# 	gender = models.CharField(max_length=2,choices=(('M','Male'),('F','Female')))
# 	quantity = models.PositiveIntegerField(default=0)
# 	sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=200, null=False)
# 	transport_cost= models.IntegerField(default=0)
# 	created = models.DateTimeField(auto_now_add=True)
# 	updated = models.DateTimeField(auto_now=True)

# 	class Meta:
# 		ordering = ('name',)
# 		index_together = (('id', 'slug'),)

# 	def __str__(self):
# 		return self.name

# 	def __unicode__(self):
# 		return self.name

# # class OrderItem(models.Model):
# # 	order = models.ForeignKey(Order, related_name='items')
# # 	product = models.ForeignKey(Product, related_name='order_items')
# # 	price = models.DecimalField(max_digits=10, decimal_places=2)
# # 	quantity = models.PositiveIntegerField(default=1)

# # 	def __str__(self):
# # 		return ("{}".format(self.id))

# # 	def get_cost(self):
# # 		return self.price * self.quantity