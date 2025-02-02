from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)  
    answer_bn = RichTextField(blank=True, null=True)
    question_es = models.TextField(blank=True, null=True)  
    answer_es = RichTextField(null=True, blank=True)
    question_fr = models.TextField(blank=True, null=True) 
    answer_fr = RichTextField(null=True, blank=True)
    question_ar = models.TextField(blank=True, null=True) 
    answer_ar = RichTextField(null=True, blank=True)
    question_pt = models.TextField(blank=True, null=True) 
    answer_pt = RichTextField(null=True, blank=True)
    question_ru = models.TextField(blank=True, null=True) 
    answer_ru = RichTextField(null=True, blank=True)
    question_de = models.TextField(blank=True, null=True)  
    answer_de = RichTextField(null=True, blank=True)
    question_ja = models.TextField(blank=True, null=True) 
    answer_ja = RichTextField(null=True, blank=True)
    question_ko = models.TextField(blank=True, null=True)  
    answer_ko = RichTextField(null=True, blank=True)
    question_it = models.TextField(blank=True, null=True)  
    answer_it = RichTextField(null=True, blank=True)
    def __str__(self):
        return self.question

    def get_translated_text(self, lang='en'):
        cache_key = f"faq_{self.id}_{lang}"
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        translator = Translator()
        question_translation = getattr(self, f"question_{lang}", self.question)
        answer_translation = getattr(self, f"answer_{lang}", self.answer)

        if not question_translation or not answer_translation:
            question_translation = translator.translate(
                self.question, dest=lang).text
            answer_translation = translator.translate(
                self.answer, dest=lang).text

        cache.set(cache_key, {'question': question_translation,
                  'answer': answer_translation}, timeout=60*15)

        return {'question': question_translation, 'answer': answer_translation}
