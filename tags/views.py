from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import MyTags
from .serializers import TagsSerializer

@api_view(['GET'])
def tags_list_user(request):
    if request.user.is_authenticated:
        tags=MyTags.objects.filter(TagsUser=request.user.get_username())
        tagseriaizer=TagsSerializer(tags,many=True)
        return Response(status=status.HTTP_200_OK, data=tagseriaizer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['DELETE'])
def tags_del_user_lang_title(request):
    if request.user.is_authenticated:
        txt=MyTags.objects.filter(TagsUser=request.user.get_username()).filter(T2Text=request.GET['tagTxT'])
        txt.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['UPDATE'])
def tags_update_user_lang_title(request):
    if request.user.is_authenticated:
        txt=MyTags.objects.filter(TagsUser=request.user.get_username()).filter(T2Text=request.GET['tagTxT'])
        data=TagsSerializer(txt)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def tags_save_user_lang_title(request):
    if request.user.is_authenticated:
        data=TagsSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)