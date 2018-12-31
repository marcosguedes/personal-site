# -*- encoding: utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import logging
from .models import Post
from bakery.views.list import BuildableListView
from bakery.views.detail import BuildableDetailView
from django.shortcuts import get_object_or_404

log = logging.getLogger(__name__)


class PostListView(BuildableListView):
    model = Post
    queryset = Post.objects.published()


class TagPostListView(BuildableListView):
    model = Post
    queryset = Post.objects.published()

    def get_queryset(self):
        tag_slug = self.kwargs["slug"]
        return self.queryset.filter(tags__slug=tag_slug)


class PostDetailView(BuildableDetailView):
    model = Post
   
    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.published:
            return obj
        raise Http404()
