from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', browse_view, name='browse'),
    url(r'^herb/(?P<slug>[\w-]+)/$', herb_detail, name='herb'),
]
