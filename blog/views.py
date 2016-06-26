from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages

from .models import *
from .forms import *

# Create your views here.


def posts_list(request):
    page_title = "Natural Remedies"
    posts = Post.objects.all()
    categories = Category.objects.all().order_by('name')

    posts_by_tag = []
    posts_by_title = []
    posts_by_content = []

    category_id = request.GET.get('c')
    if category_id:
        posts = posts.filter(categories__id=category_id)

    q = request.GET.get('q')
    if q:
        for qw in q.split(' '):  
            # search in tags
            posts_by_tag = [x for x in posts.filter(tags__icontains=qw)]
            # search in title
            posts_by_title = [x for x in posts.filter(title__icontains=qw)]
            # search in content
            posts_by_title = [x for x in posts.filter(content__icontains=qw)]
        # make unique list
        posts = posts_by_tag
        posts.extend([p for p in posts_by_title if p not in posts])
        posts.extend([p for p in posts_by_content if p not in posts])

    

    paginator = Paginator(posts, 4)
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
        'page_var': page_var,
    }

    if category_id:
        context['category_selected'] = int(category_id)

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
            review, is_created = Review.objects.get_or_create(
                user=user, post=post, defaults={'star': star, 'comment': comment})
            review.star = star
            review.comment = comment
            review.save()
        else:
            messages.error(request, "Invalid form data!")
        return HttpResponseRedirect(post.get_absolute_url())

    if request.user.is_authenticated():
        reviews = post.reviews().filter(~Q(user__id=request.user.id))
        context['reviews'] = reviews[0:5]
        review = reviews.filter(user__id=request.user.id)
        context['review'] = review
    else:
        context['reviews'] = post.reviews()[0:5]

    return render(request, 'post_detail.html', context)
