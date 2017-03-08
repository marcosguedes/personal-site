# -*- encoding: utf-8 -*-
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import logging
from .models import Interest
from bakery.views.detail import BuildableDetailView

log = logging.getLogger(__name__)


class InterestDetailView(BuildableDetailView):
    model = Interest

    def get_queryset(self):
        qs = super(InterestDetailView, self).get_queryset()
        return qs.filter(active=True)
