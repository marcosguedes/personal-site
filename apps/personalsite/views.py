# -*- encoding: utf-8 -*-
from .models import AboutPage, HomePage
import logging
from bakery.views.detail import BuildableDetailView
from blog.models import Post

log = logging.getLogger(__name__)


class HomePageView(BuildableDetailView):
    template_name = "index.html"
    model = HomePage

    def get_object(self, queryset=None):
        return HomePage.get_solo()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.published()[:10]
        if Post.objects.published().count() > 10:
            context["load_posts"] = True
        return context


class AboutPageView(BuildableDetailView):
    model = AboutPage
    template_name = "about.html"
    build_path = "about.html"

    def get_object(self, queryset=None):
        return AboutPage.get_solo()

