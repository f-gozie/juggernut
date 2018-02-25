# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sweet.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST

@require_POST
def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Prodcut, id=product_id)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		clean = form.cleaned_data
		cart.add(product=product, quantity=clean['quantity'], update_quantity=clean['update'])
	return redirect("sweet:product_view")

# def cart_clear(request):
# 	cart = Cart(request)
# 	product = Product.objects.all()
# 	cart.remove(product)
# 	return redirect("cart:cart_detail")

# def cart_remove(request):
# 	cart = Cart(request)
# 	product = get_object_or_404(Product, id=product_id)
# 	cart.remove(product)
# 	return redirect("cart:cart_detail")

def cart_detail(request):
	cart = Cart(request)
	return render(request, 'cart/detail.html', {'cart':cart})


# Integrating 