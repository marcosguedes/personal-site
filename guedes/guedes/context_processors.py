from django.conf import settings # import the settings file

def is_debug(request):
    """
    returns DEBUG value on the template.
    EXAMPLE: 
    
    """
    return {'is_DEBUG': settings.DEBUG}