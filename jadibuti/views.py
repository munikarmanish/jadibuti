from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view (request):
    context = {
        'page_title':'Home'
    }
    #return HttpResponse('<h1>Home Page</h1>')
    return render (request, 'home_page.html',context)
