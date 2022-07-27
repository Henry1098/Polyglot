from django.db import models

# Create your models here.
class AppSetting(models.Model):
    StKey=models.CharField(max_length=40)
    StValue=models.CharField(max_length=40)
    