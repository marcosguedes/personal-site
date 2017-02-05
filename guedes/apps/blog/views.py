# -*- encoding: utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import logging
from .models import Post

log = logging.getLogger(__name__)


class PostListView(ListView):
    model = Post


class TagPostListView(ListView):
    model = Post
    
    def get_queryset(self):
        tag_slug = self.kwargs["slug"]
        return Post.objects.published().filter(tags__slug=tag_slug)


class PostDetailView(DetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        try:
            self.model.objects.get(slug=kwargs['slug'], published=True)           
            return super(PostDetailView, self).get(request, **kwargs)
        except ObjectDoesNotExist:
            # https://realpython.com/blog/python/the-most-diabolical-python-antipattern
            log.error("Post doesn't exist or is unpublished")
            raise Http404
