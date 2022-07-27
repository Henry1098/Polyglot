from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Language
from .serializers import LanguageSerializer
from accounts.models import Learner

@api_view(['GET'])
def lang_list(request):
    La=Language.objects.all()
    Laseriaizer=LanguageSerializer(La,many=True)
    return Response(status=status.HTTP_200_OK, data=Laseriaizer.data)

@api_view(['POST'])
def setting_lang(request):
    obj,created=Learner.objects.update_or_create(defaults={
        "user":request.user,
        'SelLanguage':request.POST['lang']
    })
    return Response(status=status.HTTP_200_OK if created else status.HTTP_500_INTERNAL_SERVER_ERROR)
