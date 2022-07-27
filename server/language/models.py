from django.db import models

# Create your models here.
class Language(models.Model):
    LgName=models.CharField(max_length=40)
    LgDict1URI=models.CharField(max_length=200)
    LgDict2URI=models.CharField(max_length=200)
    LgGoogleTranslateURI=models.CharField(max_length=200)
    LgExportTemplate=models.CharField(max_length=1000)
    LgTextSize=models.IntegerField()
    LgRemoveSpaces=models.IntegerField()
    LgRightToLeft=models.IntegerField()