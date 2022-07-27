from tkinter import CASCADE
from django.db import models
from accounts.models import Learner
from texts.models import MyTexts
from language.models import Language

# Create your models here.
class MyTags(models.Model):
    T2Text=models.CharField(max_length=30)
    T2Comment=models.CharField(max_length=200)
    TagsUser=models.OneToOneField(Learner, on_delete=models.CASCADE)
    TagsText=models.OneToOneField(MyTexts,on_delete=models.CASCADE)
    TagsLang=models.OneToOneField(Language,on_delete=models.CASCADE)
    TagsArchived=models.BooleanField()