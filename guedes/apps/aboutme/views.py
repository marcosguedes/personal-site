# -*- encoding: utf-8 -*-
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import logging
from .models import Interest

log = logging.getLogger(__name__)


class InterestDetailView(DetailView):
    model = Interest

    def get(self, request, *args, **kwargs):
        try:
            self.model.objects.get(slug=kwargs['slug'], active=True)           
            return super(InterestDetailView, self).get(request, **kwargs)
        except ObjectDoesNotExist:
            # https://realpython.com/blog/python/the-most-diabolical-python-antipattern
            log.error('Interest does not exist!')
            raise Http404
