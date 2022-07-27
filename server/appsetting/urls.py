from appsetting import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^settings/$', views.setting_list),
    re_path(r'^settings/ss$', views.setting_update),
]