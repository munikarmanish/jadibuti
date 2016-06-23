from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Post


# Create your views here.

def posts_list (request):
    post_data_list = Post.objects.all()

    search_query = request.GET.get('q')
    if search_query:
        post_data_list = post_data_list.filter(Q(title__icontains=search_query) |
            Q(content__icontains=search_query)).distinct()

    paginator = Paginator (post_data_list, 1)
    page_request_var = 'page'
    page_no = request.GET.get(page_request_var)

    try:
        data_list = paginator.page(page_no)
    except PageNotAnInteger:
        data_list = paginator.page(1)
    except EmptyPage:
        data_list = paginator.page(paginator.num_pages)

    context = {
        'page_title':'blog',
        'data_list':data_list,
        'page_request_var':page_request_var,
    }

    return render(request, 'posts_list.html', context)

def post_detail(request,slug=None):
    data = get_object_or_404(Post,slug=slug)
    context = {
        'page_title':data.title,
        'data':data,
    }

    return render(request, 'post_detail.html', context)
