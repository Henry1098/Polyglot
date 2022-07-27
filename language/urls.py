from language import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^language/$', views.lang_list),
    re_path(r'^language/<str:lang>/$', views.setting_lang),
]