from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer
from django.http import JsonResponse


@api_view(['GET'])
def faq_list(request):
    lang = request.GET.get('lang', 'en') 
    faqs = FAQ.objects.all()

    faq_data = [faq.get_translated(lang)
                for faq in faqs] 

    return Response(faq_data, status=status.HTTP_200_OK)

