from django.shortcuts import render

# Create your views here.


def browse_view (response):
    context = {
        'page_title':'browse',
    }
    
    return render (response, 'browse_herbs.html', context)

def herb_detail (response,slug):
	
	herb = get_object_or_404(Herb, slug=slug)

	context = {
		'page_title':'herb_detail',
		'herb':herb
	}

	return render (response, 'herb_detail.html', context)

