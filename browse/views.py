from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import *


def browse_view(response):

    herbs = Herb.objects.all()

    context = {
        'page_title': 'Herbs',
        'herbs': herbs
    }

    return render(response, 'browse_herbs.html', context)


def herb_detail(response, slug):

    herb = get_object_or_404(Herb, id=slug)

    context = {
        'herb': herb
    }

    return render(response, 'herb_detail.html', context)
