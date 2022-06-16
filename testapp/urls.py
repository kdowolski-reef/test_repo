from django.urls import re_path

from .views import testview, testhtml

urlpatterns = [
    re_path(r"login/", testview),
    re_path(r"html/", testhtml),
]
