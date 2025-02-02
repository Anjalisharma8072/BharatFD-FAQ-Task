from django.db import models
from ckeditor.fields import RichTextField
from deep_translator import GoogleTranslator


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    question_bn = models.TextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)

    question_hi = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)

    question_es = models.TextField(null=True, blank=True)
    answer_es = RichTextField(null=True, blank=True)

    question_fr = models.TextField(null=True, blank=True)
    answer_fr = RichTextField(null=True, blank=True)

    question_de = models.TextField(null=True, blank=True)
    answer_de = RichTextField(null=True, blank=True)

    question_it = models.TextField(null=True, blank=True)
    answer_it = RichTextField(null=True, blank=True)

    question_pt = models.TextField(null=True, blank=True)
    answer_pt = RichTextField(null=True, blank=True)

    question_ar = models.TextField(null=True, blank=True)
    answer_ar = RichTextField(null=True, blank=True)

    question_zh = models.TextField(null=True, blank=True)
    answer_zh = RichTextField(null=True, blank=True)

    question_ja = models.TextField(null=True, blank=True)
    answer_ja = RichTextField(null=True, blank=True)

    def translate_content(self):
        translator_bn = GoogleTranslator(source='auto', target='bn')
        translator_hi = GoogleTranslator(source='auto', target='hi')
        translator_es = GoogleTranslator(source='auto', target='es')
        translator_fr = GoogleTranslator(source='auto', target='fr')
        translator_de = GoogleTranslator(source='auto', target='de')
        translator_it = GoogleTranslator(source='auto', target='it')
        translator_pt = GoogleTranslator(source='auto', target='pt')
        translator_ar = GoogleTranslator(source='auto', target='ar')
        translator_zh = GoogleTranslator(source='auto', target='zh-CN')
        translator_ja = GoogleTranslator(source='auto', target='ja')

        if not self.question_bn:
            self.question_bn = translator_bn.translate(self.question)
        if not self.answer_bn:
            self.answer_bn = translator_bn.translate(self.answer)

        if not self.question_hi:
            self.question_hi = translator_hi.translate(self.question)
        if not self.answer_hi:
            self.answer_hi = translator_hi.translate(self.answer)

        if not self.question_es:
            self.question_es = translator_es.translate(self.question)
        if not self.answer_es:
            self.answer_es = translator_es.translate(self.answer)

        if not self.question_fr:
            self.question_fr = translator_fr.translate(self.question)
        if not self.answer_fr:
            self.answer_fr = translator_fr.translate(self.answer)

        if not self.question_de:
            self.question_de = translator_de.translate(self.question)
        if not self.answer_de:
            self.answer_de = translator_de.translate(self.answer)

        if not self.question_it:
            self.question_it = translator_it.translate(self.question)
        if not self.answer_it:
            self.answer_it = translator_it.translate(self.answer)

        if not self.question_pt:
            self.question_pt = translator_pt.translate(self.question)
        if not self.answer_pt:
            self.answer_pt = translator_pt.translate(self.answer)

        if not self.question_ar:
            self.question_ar = translator_ar.translate(self.question)
        if not self.answer_ar:
            self.answer_ar = translator_ar.translate(self.answer)

        if not self.question_zh:
            self.question_zh = translator_zh.translate(self.question)
        if not self.answer_zh:
            self.answer_zh = translator_zh.translate(self.answer)

        if not self.question_ja:
            self.question_ja = translator_ja.translate(self.question)
        if not self.answer_ja:
            self.answer_ja = translator_ja.translate(self.answer)

    def get_translated(self, lang):
        """Return translated question and answer based on the language."""
        translations = {
            'en': {'question': self.question, 'answer': self.answer},
            'bn': {'question': self.question_bn, 'answer': self.answer_bn},
            'hi': {'question': self.question_hi, 'answer': self.answer_hi},
            'es': {'question': self.question_es, 'answer': self.answer_es},
            'fr': {'question': self.question_fr, 'answer': self.answer_fr},
            'de': {'question': self.question_de, 'answer': self.answer_de},
            'it': {'question': self.question_it, 'answer': self.answer_it},
            'pt': {'question': self.question_pt, 'answer': self.answer_pt},
            'ar': {'question': self.question_ar, 'answer': self.answer_ar},
            'zh': {'question': self.question_zh, 'answer': self.answer_zh},
            'ja': {'question': self.question_ja, 'answer': self.answer_ja},
        }

        return translations.get(lang, {'question': self.question, 'answer': self.answer})

    def save(self, *args, **kwargs):
        if not self.pk: 
            self.translate_content()
        super().save(*args, **kwargs)
