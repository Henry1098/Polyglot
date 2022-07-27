from rest_framework import serializers
from  .models import Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Language
        fields=['id','LgName','LgDict1URI','LgDict2URI','LgGoogleTranslateURI','LgExportTemplate','LgTextSize','LgRemoveSpaces','LgRightToLeft']