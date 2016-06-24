from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Post


# Create your views here.

def posts_list(request):
    posts = Post.objects.all()

    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        ).distinct()

    paginator = Paginator(posts, 2)
    page_var = 'page'
    page_no = request.GET.get(page_var)

    try:
        posts = paginator.page(page_no)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'page_title': 'Natural Remedies',
        'paginator': paginator,
        'posts': posts,
        'page_var': page_var,
    }
    return render(request, 'posts_list.html', context)


def post_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)
