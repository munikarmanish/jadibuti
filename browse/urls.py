from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^herbs$', herbs_list, name='herbs'),
    url(r'^herbs/(?P<slug>[\w-]+)/$', herb_detail, name='herb'),
    url(r'^yoga$', yoga_list, name='yogas'),
    url(r'^yoga/(?P<slug>[\w-]+)/$', yoga_detail, name='yoga'),
    url(r'^shop/(?P<slug>[\w-]+)/$', shop_detail, name='shop'),
]
