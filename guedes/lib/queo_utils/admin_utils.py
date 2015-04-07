from django import forms
from cms.models.pagemodel import Page
from django.core.cache import cache


class CmsPageModelChoiceFieldMixin(forms.ModelChoiceField):
    """
    This shows a select with the complete breadcrumb
    """
    def label_from_instance(self, obj):
        # FIXME: this is slow

        cache_key = 'ancestor_id_%s' % obj.id

        if cache.get(cache_key):
            return cache.get(cache_key)

        ancestors = []
        page = obj
        ancestors.append(page.get_title())
        while page.parent:
            ancestors.append(page.parent.get_title())
            page = page.parent

        ancestors_str = ''
        try:
            ancestors.reverse()
        except:
            pass

        try:
            ancestors_str = ' > '.join(ancestors)
        except Exception as e:
            print e

        cache.set(cache_key, ancestors_str, 600)
        return cache.get(cache_key)


# def get_queryset():
#     if cache.get('all_pages'):
#         return cache.get('all_pages')
#
#     all_pages = Page.objects.public().order_by('tree_id', 'level', 'lft')
#     cache.set('all_pages', all_pages, 30)
#
#     return cache.get('all_pages')


class CmsPageAdminForm(forms.ModelForm):
    # page = CmsPageModelChoiceFieldMixin(queryset=get_queryset())
    page = CmsPageModelChoiceFieldMixin(queryset=Page.objects.public().order_by('tree_id', 'level', 'lft'))


