from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task


# Create your views here.
def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def projects(request):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects.html')

def tasks(request):
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse("<h2>Task: %s </h2>" % task.title)
    return render(request, 'tasks.html')