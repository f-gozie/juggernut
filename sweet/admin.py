# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from sweet.models import UserProfile
from django.contrib import admin
from .models import Order, Operator, Category

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'quantity', 'created', 'updated']
	list_filter = ['created', 'updated']
	list_editable = ['price', 'quantity']
	prepopulated_fields = {'slug':('name',)}

# admin.site.register(UserProfile)
admin.site.register(Order, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Operator)