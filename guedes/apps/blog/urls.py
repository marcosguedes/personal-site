from django.conf.urls import patterns, url

from django.contrib import admin
from .views import PostListView, PostDetailView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^', PostListView.as_view(), name='post_list'),
                       url(r'^(?P<slug>(.*))/$', PostDetailView.as_view(), name='post_detail'),
                       )
