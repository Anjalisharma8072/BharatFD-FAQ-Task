from django.db.models.signals import pre_save
from django.dispatch import receiver
from googletrans import Translator
from .models import FAQ


@receiver(pre_save, sender=FAQ)
def translate_faq(sender, instance, **kwargs):
    translator = Translator()
    languages = ['hi', 'bn']  # Add languages as needed

    # Translate question and answer fields
    for lang in languages:
        question_translation = translator.translate(
            instance.question, dest=lang).text
        answer_translation = translator.translate(
            instance.answer, dest=lang).text

        setattr(instance, f'question_{lang}', question_translation)
        setattr(instance, f'answer_{lang}', answer_translation)
