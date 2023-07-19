from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Task
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """all the latest todos."""
        return Task.objects.order_by('-created_at')

def add(request):
    
    if request.method == 'POST':
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        priority = request.POST.get('priority', 1)
        due_date = request.POST.get('due_date', None)
        completed = request.POST.get('completed', False) == 'on'
        category = request.POST.get('category', '')
        # time_spent = request.POST.get('time_spent', 0)
        tag = request.POST.get('tag', '')

        Task.objects.create(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
            completed=completed,
            category=category,
            # time_spent=time_spent,
            tag=tag
        )

        return redirect('todolist_app:index')

    return render(request, 'todos/create_task.html')
    
def delete(request, todo_id):
    task = get_object_or_404(Task, pk=todo_id)
    task.delete()

    return redirect('todolist_app:index')

def update(request, todo_id):
    todo = get_object_or_404(Task, pk=todo_id)
    is_completed = request.POST.get('completed', False)
    if is_completed == 'on':
        is_completed = True
    
    todo.completed = is_completed

    todo.save()
    return redirect('todolist_app:index')
