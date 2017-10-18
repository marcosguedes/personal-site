from django.conf import settings # import the settings file
from django.contrib.sites.models import Site

def is_debug(request):
    """
    returns DEBUG value on the template.
    EXAMPLE: 
    
    """
    return {'is_DEBUG': settings.DEBUG}

def site(request):
    return {'site': Site.objects.get_current()}
