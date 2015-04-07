# From http://djangosnippets.org/snippets/1259/

import re
from django import template
from django.core.urlresolvers import NoReverseMatch, reverse
from django.template.defaultfilters import slugify

register = template.Library()


@register.filter
def truncatesmart(value, limit=80):

    try:
        limit = int(limit)
    # invalid literal for int()
    except ValueError:
        # Fail silently.
        return value

    # Make sure it's unicode
    value = unicode(value)

    # Return the string itself if length is smaller or equal to the limit
    if len(value) <= limit:
        return value

    # Cut the string
    value = value[:limit]

    # Break into words and remove the last
    words = value.split(' ')[:-1]

    # Join the words and return
    return ' '.join(words)  # + '...'  # removed by yours truly, Marcos


# FROM NAU-CRM BASEVIEWS TEMPLATETAGS
@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname=None):
    try:
        pattern = '^' + reverse(pattern_or_urlname) + '$'
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path

    if pattern and re.search(pattern, path):
        return 'active'
    return ''
