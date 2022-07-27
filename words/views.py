from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import MyWords
from .serializers import WordSerializer
from accounts.models import Learner

@api_view(['GET'])
def word_list(request):
    if request.user.is_authenticated:
        wo=MyWords.objects.filter(WoUser=request.user.get_username())
        woseriaizer=WordSerializer(wo,many=True)
        return Response(status=status.HTTP_200_OK, data=woseriaizer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['DELETE'])
def word_del(request):
    if request.user.is_authenticated:
        wo=MyWords.objects.filter(WoUser=request.user.get_username()).filter(WoText=request.POST['WoText'])
        wo.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['UPDATE'])
def word_update(request):
    if request.user.is_authenticated:
        txt=MyWords.objects.filter(WoUser=request.user.get_username()).filter(WoText=request.POST['WoText'])
        data=WordSerializer(txt)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def word_save(request):
    if request.user.is_authenticated:
        data=WordSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)