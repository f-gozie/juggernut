# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.contrib import admin
# from orders.models import Order, OrderItem

# class OrderItemInline(admin.TabularInline):
# 	model = OrderItem
# 	raw_id_fields = ['product']

# class OrderAdmin(admin.ModelAdmin):
# 	list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created', 'updated']
# 	list_filter = ['paid', 'created', 'updated']
# 	inlines = [OrderItemInline]

# admin.site.register(Order, OrderAdmin)