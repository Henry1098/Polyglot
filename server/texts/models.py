from django.db import models
from accounts.models import Learner
from language.models import Language

# Create your models here.
class MyTexts(models.Model):
    TxLgID=models.IntegerField()
    TxTitle=models.CharField(max_length=300)
    TxText=models.TextField()
    TxAnnotatedText=models.TextField()
    TxAudioURI=models.CharField(max_length=200)
    TxSourceURI=models.CharField(max_length=1000)
    TxTLang=models.OneToOneField(Language, on_delete=models.CASCADE)
    TxtUser=models.OneToOneField(Learner, on_delete=models.CASCADE)
    TxtArchived=models.BooleanField(default=False)