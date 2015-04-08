# -*- encoding: utf-8 -*-
from .models import HomePage
from django.views.generic.detail import DetailView
# from django.views.generic.detail import DetailView


class HomePageView(DetailView):
    model = HomePage
    template_name = "index.html"
