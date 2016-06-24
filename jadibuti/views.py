from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

from browse.models import CarouselImage

def home_view (request):
	carousel_data = CarouselImage.objects.filter(show=True)
	d_range = list(range(len(carousel_data)))
	zipped = zip(d_range, carousel_data)

	context = {
		'carousel_data':carousel_data,
		'page_title':'home',
		'd_range':d_range,
		'marked_active':False,
		'zipped_data':zipped,
	}
	
	return render (request, 'home_page.html', context)
