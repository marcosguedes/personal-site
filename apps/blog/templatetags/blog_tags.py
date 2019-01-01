# -*- coding: utf-8 -*-
from django import template

from ..models import Tag

register = template.Library()


@register.inclusion_tag("blog/partials/tag_menu.html", takes_context=True)
def render_tag_menu(context, tag_list=None):
    context["tag_list"] = Tag.objects.all()
    context["active_tags"] = tag_list
    return context
