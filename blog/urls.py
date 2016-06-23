from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', posts_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
]
