from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
# Create your views here.

def index(request):
    
    # for display all todo
    tasks = Todo.objects.all()
    
    # create a new todo
    if request.method == "POST":
        
        title = request.POST.get('title')
        
        if title:
            Todo.objects.create(title=title)
            
        return redirect('index')
    
    # Editing the existing todo
    if request.method == "GET" and request.GET.get('edit'):
        
        edit_task = get_object_or_404(Todo, id=request.GET.get('edit'))
        
        return render(request, 'index.html', {
            'tasks' : tasks,
            'edit_task' : edit_task
        })
    
    return render(request, 'index.html', {'tasks': tasks})

# update a todo
def update_todo(request, id):
    task = get_object_or_404(Todo, id=id)
    
    if request.method == "POST":
        
        task.title = request.POST.get('title')
        
        task.save()
    
    return redirect('index')


# delete a todo
def delete_todo(request, id):
    
    task = get_object_or_404(Todo, id=id)
    
    task.delete()
    
    return redirect('index')

# complete a todo (strike-through)
def complete(request, id):
    
    task = get_object_or_404(Todo, id=id)
    
    task.complete = not task.complete
    
    task.save()
    
    return redirect('index')