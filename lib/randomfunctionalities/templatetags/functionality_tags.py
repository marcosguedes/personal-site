# -*- coding: utf-8 -*-
from django import template

from ..models import Microformat, Network
from django.core.exceptions import ObjectDoesNotExist
import logging

register = template.Library()
log = logging.getLogger(__name__)


@register.inclusion_tag('randomfunctionalities/microformats.html', takes_context=True)
def render_microformat(context):

    try:
        context['opengraph'] = Microformat.objects.get()
    except Microformat.DoesNotExist:
        log.info('No microformats assigned')
        pass

    return context


@register.assignment_tag()
def get_microformat():
    try:
        return Microformat.objects.get()
    except Microformat.DoesNotExist:
        log.info('No microformats assigned')
        return None


@register.inclusion_tag('randomfunctionalities/networking.html', takes_context=True)
def render_networking(context):
    context['network_list'] = Network.objects.all()

    return context
