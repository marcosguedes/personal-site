# -*- coding: utf-8 -*-
from django import template

from ..models import Microformat, Network
from django.core.exceptions import ObjectDoesNotExist
import logging

register = template.Library()
log = logging.getLogger(__name__)


@register.inclusion_tag('randomfunctionalities/microformats.html', takes_context=True)
def render_microformat(context):

    microformats = None

    try:
        microformats = Microformat.objects.get()
    except ObjectDoesNotExist:
        log.warning('No microformats assigned')

    context['mformat'] = microformats

    return context


@register.inclusion_tag('randomfunctionalities/networking.html', takes_context=True)
def render_networking(context):
    context['object_list'] = Network.objects.all()

    return context
