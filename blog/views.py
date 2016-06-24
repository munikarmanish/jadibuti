from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import *


# Create your views here.

def posts_list(request):
    page_title = "Natural Remedies"
    posts = Post.objects.all()
    total_posts = posts.count()
    categories = Category.objects.all()

    # all categories to list in side panel
    # make categories a list of category string
    # to make it different from category of database
    categories = Category.objects.all()
    category_selected = request.GET.get('category')

    #posts = posts.filter(category)
    search_query = request.GET.get('q')
    if search_query:
        page_title = "Search results"
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        ).distinct()

    # filter category as well
    category_id = request.GET.get('c')
    if category_id:
        posts = posts.filter(categories__id=category_id)

    paginator = Paginator(posts, 1)
    page_var = 'page'
    page_no = request.GET.get(page_var)

    try:
        posts = paginator.page(page_no)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'page_title': page_title,
        'categories': categories,
        'paginator': paginator,
        'posts': posts,
        'total_posts': total_posts,
        'page_var': page_var,
    }
    return render(request, 'posts_list.html', context)


def post_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)
