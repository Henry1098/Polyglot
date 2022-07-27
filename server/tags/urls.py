from tags import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^tags/all$', views.tags_list_user),
    re_path(r'^tags/all/<str:tagTxT>/$', views.tags_del_user_lang_title),
    re_path(r'^tags/all/<str:tagTxT>/$', views.tags_update_user_lang_title),
    re_path(r'^tags/del/<str:tagTxT>/$', views.tags_save_user_lang_title)
]