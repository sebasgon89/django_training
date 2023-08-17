from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task


# Create your views here.
def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)


def about(request):
    return HttpResponse("<h2>About</h2>")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse("<h2>Task: %s </h2>" % task.title)