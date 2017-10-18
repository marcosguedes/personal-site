# -*- coding: utf-8 -*-
from django import template

from ..models import Interest, Category

register = template.Library()


@register.inclusion_tag('aboutme/partials/interests.html', takes_context=True)
def show_interest_masonry(context):
    interests = Interest.objects.active().filter(category__active=True)
    categories = Category.objects.filter(id__in=interests.values_list('category', flat=True).distinct())

    context['interests'] = interests
    context['categories'] = categories

    return context
