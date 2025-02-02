from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id',  'question_hi',
                  'question_bn',
                  'question_es',
                  'question_fr',
                  'question_ar',
                  'question_pt',
                  'question_ru',
                  'question_de',
                  'question_ja',
                  'question_zh',
                  'question_ko',
                  'question_it',
                  'answer_hi',
                  'answer_bn',
                  'answer_es',
                  'answer_fr',
                  'answer_ar',
                  'answer_pt',
                  'answer_ru',
                  'answer_de',
                  'answer_ja',
                  'answer_zh',
                  'answer_ko',
                  'answer_it',
                  ]
