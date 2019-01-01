from django.conf.urls import url

from django.contrib import admin
from .views import PostListView, TagPostListView, PostDetailView

admin.autodiscover()

urlpatterns = [
    url(r'^tags/(?P<slug>(.*))/$', TagPostListView.as_view(), name='tag_post_list'),
    url(r'^(?P<slug>(.*))/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^$', PostListView.as_view(), name='post_list'),
]