from django.db import models
from accounts.models import Learner
from language.models import Language
from texts.models import MyTexts

# Create your models here.
class MyWords(models.Model):
    WoLgID=models.IntegerField()
    WoText=models.CharField(max_length=1000)
    WoTextLC=models.CharField(max_length=1000)
    WoStatus=models.IntegerField(max_length=5)
    WoTranslation=models.CharField(max_length=1000)
    WoRomanization=models.CharField(max_length=200)
    WoSentence=models.CharField(max_length=1000)
    WoCreated=models.DateField()
    WoStatusChanged=models.DateField()
    WoTodayScore=models.FloatField()
    WoTomorrowScore=models.FloatField()
    WoRandom=models.FloatField()
    WoGrammar=models.CharField(max_length=1000)
    WoPos=models.CharField(max_length=30)
    WoUser=models.OneToOneField(Learner,on_delete=models.CASCADE)
    WoLang=models.OneToOneField(Language,on_delete=models.CASCADE)
    WoTxt=models.OneToOneField(MyTexts,on_delete=models.CASCADE)