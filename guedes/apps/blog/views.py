# -*- encoding: utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import logging
from .models import Post
from bakery.views.list import BuildableListView
from bakery.views.detail import BuildableDetailView

log = logging.getLogger(__name__)


class PostListView(BuildableListView):
    model = Post


class TagPostListView(BuildableListView):
    model = Post
    
    def get_queryset(self):
        tag_slug = self.kwargs["slug"]
        return Post.objects.published().filter(tags__slug=tag_slug)


class PostDetailView(BuildableDetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        try:
            self.model.objects.get(slug=kwargs['slug'], published=True)           
            return super(PostDetailView, self).get(request, **kwargs)
        except ObjectDoesNotExist:
            # https://realpython.com/blog/python/the-most-diabolical-python-antipattern
            log.error("Post doesn't exist or is unpublished")
            raise Http404
