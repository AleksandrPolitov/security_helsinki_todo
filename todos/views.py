from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Todo

def index(request):
    # FIX (3)
    # if not request.user.is_authenticated:
    #     return redirect('login')
    # todos = Todo.objects.filter(user=request.user)
    # return render(request, 'todos/index.html', {'todos': todos})

    # without auth:
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})


# @csrf_exempt # FIX (2)
# def add(request):
#     # FIX (3)
#     if not request.user.is_authenticated:
#         return redirect('login')
#     if request.method == 'POST':
#         text = request.POST.get('text')
#         if text:
#             Todo.objects.create(text=text, user=request.user)
#     return redirect('index')

# without auth:
@csrf_exempt # FIX (2)
def add(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Todo.objects.create(text=text)
    return redirect('index')


def delete(request, todo_id):
    # FIX (4)
    # if not request.user.is_authenticated:
    #     return redirect('login')
    # todo = Todo.objects.get(id=todo_id, user=request.user)
    # todo.delete()
    # return redirect('index')

    # without auth:
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')


def toggle(request, todo_id):
    # FIX (4)
    # if not request.user.is_authenticated:
    #     return redirect('login')
    # todo = Todo.objects.get(id=todo_id, user=request.user)
    # todo.done = not todo.done
    # todo.save()
    # return redirect('index')

    # without auth:
    todo = Todo.objects.get(id=todo_id)
    todo.done = not todo.done
    todo.save()
    return redirect('index')
