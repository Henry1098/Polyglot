from rest_framework import serializers
from  .models import MyTexts

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyTexts
        fields=['id',"TxLgID","TxTitle","TxText","TxAnnotatedText","TxAudioURI","TxSourceURI","TxTLang","TxtUser","TxtArchived"]