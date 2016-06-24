from django.shortcuts import render

# Create your views here.


def browse_view (response):
    context = {
        'page_title':'browse',
    }
    
    return render (response, 'browse_herbs.html', context)
