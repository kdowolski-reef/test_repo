from django.shortcuts import render

from django.http import HttpResponse


def testview(r):
    return HttpResponse("abc")


def testhtml(r):
    return render(r, "test.html", context={"user": "a@a.pl"})
