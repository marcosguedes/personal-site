# -*- encoding: utf-8 -*-
from .models import HomePage
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import logging

log = logging.getLogger(__name__)


class HomePageView(DetailView):
    model = HomePage
    template_name = "index.html"

    def get_object(self, queryset=None):
        try:
            return HomePage.objects.get()
        except ObjectDoesNotExist:
            # print "Homepage not created"
            log.error('Homepage not created!')
            raise Http404
