from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

def index(request):
    todos = Todo.objects.all()[:10] # gets all todos from model

    context = {
        'todos': todos # to pass them to index.html
    }

    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')

def edit(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }

    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        if len(str(title)) != 0:
            todo.title = title

        if len(str(text)) != 0:
            todo.text = text

        todo.save()

        return redirect('/todos')

    else:
        return render(request, 'edit.html', context)

def delete(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }

    if(request.method == 'POST'):
        Todo.delete(todo)
        return redirect('/todos')
    else:
        return render(request, 'delete.html', context)
