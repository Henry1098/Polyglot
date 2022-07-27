from words import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^words/all/$', views.word_list),
    re_path(r'^words/del/<str:WoText>/$', views.word_del),
    re_path(r'^words/update/<str:WoText>/$', views.word_update),
    re_path(r'^words/save/$', views.word_save)
]