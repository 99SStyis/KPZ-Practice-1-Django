from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'common/task_create.html', {'form': form})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'common/task_list.html', {'tasks': tasks})
