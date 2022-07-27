from django.db import models
from django.contrib.auth.models import User
from language.models import Language

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    SelLanguage=models.OneToOneField(Language,on_delete=models.CASCADE)