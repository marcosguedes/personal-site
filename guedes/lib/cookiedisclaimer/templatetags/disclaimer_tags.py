from django import template
from ..models import CookieDisclaimer
import logging

log = logging.getLogger(__name__)

register = template.Library()


def show_disclaimer(context):

    context['disclaimer'] = None

    try:
        context['disclaimer'] = CookieDisclaimer.objects.get()
    except Exception as e:
        log.error('Disclaimer not created! Error: %s' % e)
        pass

    return context

register.inclusion_tag('cookiedisclaimer/cookiedisclaimer.html', takes_context=True)(show_disclaimer)
