from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import *

def search_posts (search_query, posts):
    sq = search_query.split ()
    result = []

    for s in sq:
        result.append('hi')

# Create your views here.

def posts_list(request):
    page_title = "Natural Remedies"
    posts = Post.objects.all()
    total_posts = posts.count()
    categories = Category.objects.all()
    query_list =[]
    unique_query_list=[]

    # all categories to list in side panel
    # make categories a list of category string
    # to make it different from category of database
    categories = Category.objects.all()
    category_selected = request.GET.get('category')

    #posts = posts.filter(category)
    search_query = request.GET.get('q')

#    splitted_search_query=[]
    splitted_search_query = search_query.split(" ")
    for something in splitted_search_query:
        if something not in unique_query_list:
            unique_query_list.append(something)
    splitted_search_query = unique_query_list

    if search_query:
        page_title = "Search results"
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        ).distinct()
    if not posts:
        for words in splitted_search_query:
            posts = Post.objects.all()
            posts = posts.filter(Q(title__icontains=words) | Q(content__icontains=words)).distinct()
            query_list.append(posts)


    paginator = Paginator(posts, 6)
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
        'categories':categories,
        'paginator': paginator,
        'posts': posts,
        'total_posts': total_posts,
        'categories': categories,
        'page_var': page_var,
        'splitted_search_query':splitted_search_query,
        'query_list': query_list
    }
    return render(request, 'posts_list.html', context)


def post_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)
