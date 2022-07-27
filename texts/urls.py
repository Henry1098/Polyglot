from texts.views import lang_save_user_lang_title
from texts import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^texts/all/$', views.lang_list_user),
    re_path(r'^texts/all/<str:lang>/$', views.lang_list_user_lang),
    re_path(r'^texts/all/<str:lang>/<str:title>/$', views.lang_list_user_lang_title),
    re_path(r'^texts/del/<str:lang>/<str:title>/$', views.lang_del_user_lang_title),
    re_path(r'^texts/update/<str:lang>/<str:title>/$', views.lang_update_user_lang_title),
    re_path(r'^texts/save/<str:lang>/<str:title>/$', views.lang_save_user_lang_title),
    re_path(r'^texts/saveOp/<str:lang>/<str:title>/$', views.lang_save_open_user_lang_title),
    re_path(r'^texts/archive/all/$', views.lang_list_user_archived),
    re_path(r'^texts/archive/all/<str:lang>/$', views.lang_list_user_lang_archived),
    re_path(r'^texts/archive/all/<str:lang>/<str:title>/$', views.lang_list_user_lang_title_archived),
    re_path(r'^texts/archive/del/<str:lang>/<str:title>/$', views.lang_del_user_lang_title_archived),
    re_path(r'^texts/archive/update/<str:lang>/<str:title>/$', views.lang_update_user_lang_title_archived),
    re_path(r'^texts/archive/save/<str:lang>/<str:title>/$', views.lang_save_user_lang_title_archived),
]