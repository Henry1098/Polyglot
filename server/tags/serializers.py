from rest_framework import serializers
from  .models import MyTags

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyTags
        fields=['id',"T2Text","T2Comment","TagsLang","TagsUser","TagsText","TagsLang","TagsArchived"]