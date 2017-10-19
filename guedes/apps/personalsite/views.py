# -*- encoding: utf-8 -*-
from .models import HomePage
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import logging
from aboutme.models import Category
from bakery.views.detail import BuildableDetailView
from django.views.decorators.csrf import csrf_exempt

log = logging.getLogger(__name__)


class HomePageView(BuildableDetailView):
    model = HomePage
    template_name = "index.html"

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(HomePageView,self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        try:
            return HomePage.objects.get()
        except ObjectDoesNotExist:
            # https://realpython.com/blog/python/the-most-diabolical-python-antipattern
            log.error('Homepage not created!')
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(active=True)

        return context
