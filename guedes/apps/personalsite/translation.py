from modeltranslation.translator import translator, TranslationOptions
from .models import HomePage


class HomePageTranslationOptions(TranslationOptions):
    fields = ('page_title', 'meta_description', )


translator.register(HomePage, HomePageTranslationOptions)
