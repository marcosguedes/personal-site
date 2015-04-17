from modeltranslation.translator import translator, TranslationOptions
from .models import Microformat


class MicroformatTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'workplace', 'description')


translator.register(Microformat, MicroformatTranslationOptions)
