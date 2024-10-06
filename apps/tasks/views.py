from django.shortcuts import render
from django.views.generic import DetailView
from tasks.models import Task

class TaskView(DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = 'task'
