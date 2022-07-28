import json
from tkinter import E
from django.shortcuts import render
from tags.models import MyTags
from words.models import MyWords
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import MyTexts
from .serializers import TextSerializer
from accounts.models import Learner
#from .utilities import Utilities

@api_view(['GET'])
def lang_list_user(request):
    #util=Utilities()
    #data={"data":util.am("በኢትዮጵያ ጉብኝት ያደረጉት የአውሮፓ ኅብረት ከፍተኛ ባለሥልጣን፣ መንግሥት በትግራይ ለአንድ ዓመት ያህል ተቋርጠው የቆዩት መሠረታዊ አገልግሎቶች መልሰው እንዲጀመሩ ማድረግ አለበት አሉ።")}
    #data=json.dumps(data,ensure_ascii=False)
    #print(data)
    txt=MyTexts.objects.filter(TxtUser=request.user.id)
    txtseriaizer=TextSerializer(txt,many=True)
    return Response(status=status.HTTP_200_OK, data=txtseriaizer.data)

@api_view(['GET'])
def lang_list_user_lang(request):
    txt=MyTexts.objects.filter(TxtUser=request.user.id).filter(TxTLang=request.GET['lang']).exclude(TxtArchived=True)
    txtseriaizer=TextSerializer(txt,many=True)
    return Response(status=status.HTTP_200_OK, data=txtseriaizer.data)
    

@api_view(['GET'])
def lang_list_user_lang_title(request):
    txt=MyTexts.objects.filter(TxtUser=request.user.id).filter(TxTLang=request.GET['lang']).filter(TxTitle=request.GET['title']).exclude(TxtArchived=True)
    txtseriaizer=TextSerializer(txt)
    return Response(status=status.HTTP_200_OK, data=txtseriaizer.data)
    

@api_view(['DELETE'])
def lang_del_user_lang_title(request):
    txt=MyTexts.objects.filter(TxtUser=request.user.id).filter(TxTLang=request.GET['lang']).filter(TxTitle=request.GET['title']).exclude(TxtArchived=True)
    tag=MyTags.objects.filter(TagsUser=request.user).filter(TagsText=txt).exclude(TxtArchived=True)
    wo=MyWords.objects.filter(WoUser=request.user).filter(WoTxt=txt).exclude(TxtArchived=True)
    txt.delete()
    tag.delete()
    wo.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['UPDATE'])
def lang_update_user_lang_title(request):
    txt=MyTexts.objects.filter(TxtUser=request.user.id).filter(TxTitle=request.GET['title'])
    data=TextSerializer(txt)
    if data.is_valid():
        data.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def lang_save_user_lang_title(request):
    data=TextSerializer(data=request.data)
    if data.is_valid():
        data.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def lang_save_open_user_lang_title(request):
    status,data=data=lang_list_user_lang_title(request)
    return Response(status=status,data=data)

@api_view(['GET'])
def lang_list_user_archived(request):
    txt=MyTexts.objects.filter(TxtUser=request.user.id).exclude(TxtArchived=False)
    txtseriaizer=TextSerializer(txt,many=True)
    return Response(status=status.HTTP_200_OK, data=txtseriaizer.data)
   
@api_view(['GET'])
def lang_list_user_lang_archived(request):
    txt=MyTexts.objects.filter(TxtUser=request.user.id).filter(TxTLang=request.GET['lang']).exclude(TxtArchived=False)
    txtseriaizer=TextSerializer(txt,many=True)
    return Response(status=status.HTTP_200_OK, data=txtseriaizer.data)
    
@api_view(['GET'])
def lang_list_user_lang_title_archived(request):
    txt=MyTexts.objects.filter(TxtUser=request.user.id).filter(TxTLang=request.GET['lang']).filter(TxTitle=request.GET['title']).exclude(TxtArchived=False)
    txtseriaizer=TextSerializer(txt)
    return Response(status=status.HTTP_200_OK, data=txtseriaizer.data)
   
@api_view(['DELETE'])
def lang_del_user_lang_title_archived(request):
    txt=MyTexts.objects.filter(TxtUser=request.user.id).filter(TxTLang=request.GET['lang']).filter(TxTitle=request.GET['title']).exclude(TxtArchived=False)
    tag=MyTags.objects.filter(TxtUser=request.user.id).filter(TxTLang=request.GET['lang']).filter(TxTitle=request.GET['title']).exclude(TxtArchived=False)
    wo=MyWords.objects.filter(TxtUser=request.user.id).filter(TxTLang=request.GET['lang']).filter(TxTitle=request.GET['title']).exclude(TxtArchived=False)
    txt.delete()
    tag.delete()
    wo.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['UPDATE'])
def lang_update_user_lang_title_archived(request):
    txt=MyTexts.objects.filter(TxtUser=request.user.id).filter(TxTitle=request.GET['title']).exclude(TxtArchived=False)
    data=TextSerializer(txt)
    if data.is_valid():
        data.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def lang_save_user_lang_title_archived(request):
    data=TextSerializer(data=request.data)
    if data.is_valid():
        data.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)