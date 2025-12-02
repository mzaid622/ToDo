from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
  lists = Task.objects.all().order_by("created_at")
  form = TaskForm()
  if request.method == "POST":
    form = TaskForm(request.POST)  # form ko POST data ke sath bind kar diya
    if form.is_valid():
      form.save()
    return redirect("/")
  return render(request,"index.html",{"lists":lists,"form":form})

def edit_page(request,id):
  task = get_object_or_404(Task, pk=id)
  form = TaskForm(instance=task)
  if request.method == "POST":
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
      return redirect("/")
  return render(request,"edit.html",{"form":form})


def delete_task(request,id):
  task = get_object_or_404(Task, pk=id)
  if request.method == "POST":
    task.delete()
    return redirect("/")
  
  return render(request,"delete.html",{"task":task})