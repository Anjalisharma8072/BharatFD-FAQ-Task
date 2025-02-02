from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Language-specific translations for question and answer
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.question

    def get_translated_text(self, lang='en'):
        # Check cache for translations
        cache_key = f"faq_{self.id}_{lang}"
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        # Otherwise, use googletrans for translation
        translator = Translator()
        question_translation = getattr(self, f"question_{lang}", self.question)
        answer_translation = getattr(self, f"answer_{lang}", self.answer)

        # Fallback to English if translation is not available
        if not question_translation or not answer_translation:
            question_translation = self.question
            answer_translation = self.answer

        # Cache the result for future requests
        cache.set(cache_key, {'question': question_translation,
                  'answer': answer_translation}, timeout=60*15)

        return {'question': question_translation, 'answer': answer_translation}
