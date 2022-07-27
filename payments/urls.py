from payments import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^test-payment/$', views.test_payment),
]