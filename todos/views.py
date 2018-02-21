from django.shortcuts import render
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
