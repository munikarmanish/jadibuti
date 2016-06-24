from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages

from .models import *
from .forms import *


def search_posts(search_query, posts):
    sq = search_query.split()
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
    test = 1
    query_list = []
    unique_query_list = []
    splitted_search_query = []

    # all categories to list in side panel
    # make categories a list of category string
    # to make it different from category of database
    categories = Category.objects.all().order_by('name')

    #posts = posts.filter(category)
    search_query = request.GET.get('q')
    #splitted_search_query=[]
    splitted_search_query = search_query.split(" ")
    for something in splitted_search_query:
        if something not in unique_query_list:
            unique_query_list.append(something)
    splitted_search_query = unique_query_list
    if search_query:
        # splitted_search_query=[]
        splitted_search_query = search_query.split(" ")
        for something in splitted_search_query:
            if something not in unique_query_list:
                unique_query_list.append(something)
        splitted_search_query = unique_query_list

        page_title = "Search results"
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        ).distinct()

    if not posts and search_query:
        for words in splitted_search_query:
            posts = Post.objects.all()
            posts = posts.filter(Q(title__icontains=words) | Q(
                content__icontains=words)).distinct()
            query_list.append(posts)
        test = 0


    # filter category as well
    category_id = request.GET.get('c')
    if category_id:
        posts = posts.filter(categories__id=category_id)

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
        'page_title': page_title,
        'categories': categories,
        'paginator': paginator,
        'posts': posts,
        'total_posts': total_posts,
        'page_var': page_var,
        'splitted_search_query':splitted_search_query,
        'query_list': query_list,
        'test':test
    }
    return render(request, 'posts_list.html', context)


def post_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post, }
    form = ReviewForm(request.POST or None)
    context['form'] = form

    if request.method == "POST":
        if form.is_valid():
            user = request.user
            star = form.cleaned_data.get('star')
            comment = form.cleaned_data.get('comment')
            review, is_created = Review.objects.get_or_create(user=user, post=post,
                defaults={'star': star, 'comment': comment})
            review.star = star
            review.comment = comment
            review.save()
        else:
            messages.error(request, "Invalid form data!")
        return HttpResponseRedirect(post.get_absolute_url())

    if request.user.is_authenticated():
        reviews = post.reviews().filter(~Q(user__id=request.user.id))
        context['reviews'] = reviews
        review = reviews.filter(user__id=request.user.id)
        context['review'] = review
    else:
        context['reviews'] = post.reviews()

    return render(request, 'post_detail.html', context)
