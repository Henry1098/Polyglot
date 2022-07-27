from rest_framework import serializers
from  .models import MyWords

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyWords
        fields=['id',"WoLgID","WoText","WoTextLC","WoStatus","WoTranslation","WoRomanization","WoSentence","WoCreated","WoStatusChanged","WoTodayScore","WoTomorrowScore","WoRandom","WoGrammar","WoPos","WoUser","WoLang","WoTxt"]