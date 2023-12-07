from django.shortcuts import render
from todo.models import Task

def home(request):
  tasks=Task.objects.all()
  completed_task = Task.objects.filter(is_completed=True)
  context={
    'tasks' : tasks,
    'completed_task':completed_task,
  }
  return render(request,'home.html',context)

