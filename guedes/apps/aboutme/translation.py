from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Interest


class BaseTranslationOptions(TranslationOptions):
    fields = ('title', )


class CategoryTranslationOptions(BaseTranslationOptions):
    fields = ('short_description', )


class InterestTranslationOptions(BaseTranslationOptions):
    fields = ('description', )


translator.register(Category, CategoryTranslationOptions)
translator.register(Interest, InterestTranslationOptions)
