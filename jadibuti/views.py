from django.shortcuts import render

# Create your views here.

def home_view (request):
    context = {
        'page_title':'Home'
        
    }
    return render (request, 'home_page.html',context)
