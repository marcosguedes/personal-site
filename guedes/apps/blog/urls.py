from django.conf.urls import patterns, url

from django.contrib import admin
from .views import PostListView, TagPostListView, PostDetailView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^post/(?P<slug>(.*))/$', PostDetailView.as_view(), name='post_detail'),
                       url(r'^(?P<slug>(.*))/$', TagPostListView.as_view(), name='tag_post_list'),
                       url(r'^$', PostListView.as_view(), name='post_list'),
                       )
