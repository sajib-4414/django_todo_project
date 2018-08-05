from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def get_index_page(request):
    todos = Todo.objects.all()[:10]
    context = {
        'name': 'Sajib',
        'todos':todos,
    }
    return render(request,'index.html',context)


def get_details_page(request,id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo,
    }
    return render(request, 'post/detail.html', context)

def add_todo(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todos')
    else:
        return render(request,'post/add.html')