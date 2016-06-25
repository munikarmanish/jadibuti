from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', browse_view, name='browse'),
    url(r'^herb/(?P<slug>[\w-]+)/$', herb_detail, name='herb'),
    url(r'^shop/(?P<slug>[\w-]+)/$', shop_detail, name='shop'),
]
