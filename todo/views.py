from django.shortcuts import render,redirect
from .models import Task


# Create your views here.
def addTask(request):
  if request.method == 'POST':
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
  

def mark_as_done(request,id):
  task=Task.objects.get(id=id)
  task.is_completed=True
  task.save()
  return redirect('home')


def edit_task(request,id):
  edit_task=Task.objects.get(id=id)
  if request.method == 'POST':
    new_task=request.POST['task']
    edit_task.task=new_task
    edit_task.save()

    return redirect('home')
  else:
    context={
      'edit_task' : edit_task
    }
    return render(request,'edit.html',context)
  

def delete_task(request,id):
  delete_task=Task.objects.get(id=id)
  delete_task.delete()
  return redirect('home')
