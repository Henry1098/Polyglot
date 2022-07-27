from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import AppSetting
from .serializers import AppSettingSerializer

@api_view(['GET'])
def setting_list(request):
    AppSet=AppSetting.objects.all()
    appseriaizer=AppSettingSerializer(AppSet,many=True)
    return Response(status=status.HTTP_200_OK, data=appseriaizer.data)


@api_view(['UPDATE'])
def setting_update(request):
    appseriaizer=AppSettingSerializer(data=request.data,many=True)
    if appseriaizer.is_valid():
        appseriaizer.save()
    return Response(status=status.HTTP_200_OK, data=appseriaizer.data)




