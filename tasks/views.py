from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("task_list")
    return render(request, "tasks/task_form.html")

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")
