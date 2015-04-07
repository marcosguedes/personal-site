import re
from classytags.arguments import Argument
from classytags.core import Tag, Options
from django import template
from cms.templatetags.cms_tags import get_placeholder_content
from cms.models import Page

register = template.Library()

class PlaceholderImageURL(Tag):
    name = 'placeholderimageurl'
    options = Options(
        Argument('placeholder_name', resolve=False),
        Argument('default_page_id', resolve=False),
    )

    def render_tag(self, context, placeholder_name, default_page_id):
        url = ""
        if not 'request' in context:
            return ''
        request = context['request']
        page = request.current_page
        content = get_placeholder_content(context, request, page, placeholder_name, True)
        if content:
            url = content[content.find('src="') + 5:]
        else:
            page = Page.objects.public().published().get(reverse_id=default_page_id)
            content = get_placeholder_content(context, request, page, placeholder_name, True)
            url = content[content.find('src="') + 5:]
        url = url[:url.find('"')]
        return url

register.tag(PlaceholderImageURL)
