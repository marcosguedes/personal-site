# -*- encoding: utf-8 -*-
from django.http import Http404
import logging
from .models import Post, Tag
from bakery.views.list import BuildableListView
from bakery.views.detail import BuildableDetailView
from django.shortcuts import get_object_or_404

log = logging.getLogger(__name__)


class PostListView(BuildableListView):
    model = Post
    queryset = Post.objects.published()
    build_path = "blog/post_list.html"


class TagPostListView(BuildableDetailView):
    model = Tag
    # queryset = Post.objects.published()
    build_path = "blog/post_tag_list.html"
    template_name = "blog/post_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        obj = get_object_or_404(self.model, slug=self.kwargs["slug"])
        ctx["object"] = obj
        ctx["object_list"] = obj.get_related_posts()
        return ctx


class PostDetailView(BuildableDetailView):
    model = Post
    build_path = "blog/post_detail.html"
   
    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.published:
            return obj
        raise Http404()
