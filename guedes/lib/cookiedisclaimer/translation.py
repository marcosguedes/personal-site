from modeltranslation.translator import translator, TranslationOptions

from .models import CookieDisclaimer


class CookieDisclaimerTranslationOptions(TranslationOptions):
    fields = ('text',)

translator.register(CookieDisclaimer, CookieDisclaimerTranslationOptions)
