# -*- coding: utf-8 -*-
from django import template

from ..models import Interest, Category

register = template.Library()


@register.inclusion_tag('aboutme/partials/interests.html', takes_context=True)
def show_interest_masonry(context):
    interests = Interest.objects.active().filter(category__active=True)
    interest_list = []
    categories = []

    [interest_list.append(interest) for interest in interests]
    interest_categories = interests.values_list('category').distinct()
    categories = Category.objects.filter(id__in=interest_categories)

    context['interest_list'] = interest_list
    context['categories'] = categories

    return context
