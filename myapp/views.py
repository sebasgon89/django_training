from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)


def about(request):
    return HttpResponse("<h2>About</h2>")
