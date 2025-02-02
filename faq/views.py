from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer


class FAQView(APIView):
    def get(self, request, *args, **kwargs):
        # Default to English if no lang is provided
        lang = request.GET.get('lang', 'en')
        faqs = FAQ.objects.all()
        faq_data = []

        for faq in faqs:
            translated_faq = faq.get_translated_text(lang)
            faq_data.append(translated_faq)

        return Response(faq_data, status=status.HTTP_200_OK)
