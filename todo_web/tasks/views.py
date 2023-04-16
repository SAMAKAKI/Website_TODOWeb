from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q


class HomeView(TemplateView):
    template_name = 'tasks/home.html'


def DonePerCent(request):
    projects = Project.objects.filter(user=request.user)
    count_tasks = 0
    count_done_tasks = 0
    for project in projects:
        if TODO.objects.filter(project=project):
            for task in TODO.objects.filter(project=project):
                if task.is_done:
                    count_done_tasks += 1
                
                count_tasks += 1
            per_cent = int((count_done_tasks/count_tasks)*100)
            project.done_per_cent = per_cent
            project.save()
 

class TODOView(View):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(user=request.user)
        DonePerCent(request)
        
        return render(request, 'tasks/todo.html', locals())

class TODOTasksView(View):
    def get(self, request, id, *args, **kwargs):
        projects = Project.objects.filter(user=request.user)
        project = Project.objects.get(user=request.user, pk=id)
        todo = TODO.objects.filter(project=project)
        DonePerCent(request)
        
        return render(request, 'tasks/todo.html', locals())

class CreateProjectView(View):
    def get(self, request, *args, **kwargs):
        form = ProjectForm()
        return render(request, 'tasks/create_project.html', locals())
    
    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            
            reg = Project(user=user, name=name)
            reg.save()
            
            return redirect('todo')
        else:
            messages.warning(request, 'Invalid Input Data')
            return render(request, 'tasks/create_project.html', locals()) 

class CreateTaskView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'tasks/create_task.html', locals())
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            project = form.cleaned_data['project']
            
            reg = TODO(name=name, project=project)
            reg.save()
            
            return redirect('todo')
        else:
            messages.warning(request, 'Invalid Input Data')
            return render(request, 'tasks/create_task.html', locals()) 

def is_done(request):
    if request.method == 'GET':
        task_id = request.GET['task_id']
        task = TODO.objects.get(pk=task_id)
        if task.is_done == False:
            task.is_done = True
            task.save()
        else:
            task.is_done = False
            task.save()
        
        
        data = {}
        return JsonResponse(data=data)