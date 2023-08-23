from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask


# Create your views here.
def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def index(request):
    title = "Django Course!"
    return render(request, 'index.html',{
        'title' : title
    })


def about(request):
    username = "Sebasgon"
    return render(request, 'about.html', {
        'username' : username,
    })

def projects(request):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        'projects' : projects
    })

def tasks(request):
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse("<h2>Task: %s </h2>" % task.title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html',{
        'tasks' : tasks
    })

def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html",{
            'form' : CreateNewTask
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'],project_id=2)
        return redirect("/tasks/")