from django.shortcuts import render

from django.http import HttpResponse


def testview(r):
    return HttpResponse("abc")
