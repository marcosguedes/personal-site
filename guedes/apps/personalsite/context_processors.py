from django.conf import settings # import the settings file
from .models import HomePage

def site(request):
    return {'site': HomePage.objects.get()}
