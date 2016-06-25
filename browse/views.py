from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.

from .models import *

def browse_view (response):

	herbs = Herb.objects.all()

	context = {
		'page_title':'browse',
		'herbs':herbs
	}
	
	return render (response, 'browse_herbs.html', context)

def herb_detail (response,slug):
	
	herb = get_object_or_404(Herb, id=slug)
	shops = herb.shops.all()
	diseases_cured = herb.disease_set.all()

	context = {
		'page_title':'herb_detail',
		'herb':herb,
		'available_in':shops,
		'diseases_cured':diseases_cured
	}

	return render (response, 'herb_detail.html', context)

def shop_detail(response, slug):
	
	shop = get_object_or_404 (HerbShop, id=slug)
	available_herbs = shop.herb_set.all()

	context = {
		'page_title':shop.name,
		'shop':shop,
		'available_herbs':available_herbs,
	}

	return render (response, 'shop_detail.html',context)