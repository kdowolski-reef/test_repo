from django.urls import re_path

from .views import testview

urlpatterns = [
    re_path(r"login/", testview),
]
