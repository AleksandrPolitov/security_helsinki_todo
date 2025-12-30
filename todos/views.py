from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
import logging

logger = logging.getLogger(__name__)

def index(request):
    # FIX (3)
    # if not request.user.is_authenticated:
    #     return redirect('login')
    # todos = Todo.objects.filter(user=request.user)
    # return render(request, 'todos/index.html', {'todos': todos})

    # FLAW (3)
    todos = Todo.objects.all()


    # FLAW (4)
    print("LOG: listing todos for user=%s count=%s" % (
                request.user.username if request.user.is_authenticated else 'none',
                todos.count()))

    # FIX (4)
    # logger.info("todos_listed user=%s count=%s",
    #             request.user.username if request.user.is_authenticated else 'none',
    #             todos.count())


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
            todo = Todo.objects.create(text=text)

            # FLAW (4)
            print("LOG: todo_created user=%s todo_id=%s text=%s" % (
                        request.user.username if request.user.is_authenticated else 'none',
                        todo.id,
                        text))

            # FIX (4) 
            # logger.info("todo_created user=%s todo_id=%s",
            #             request.user.username if request.user.is_authenticated else 'none',
            #             todo.id)

    return redirect('index')


def delete(request, todo_id):
    # FIX (3)
    # if not request.user.is_authenticated:
    #     return redirect('login')
    # todo = Todo.objects.get(id=todo_id, user=request.user)
    # todo.delete()
    # return redirect('index')

    # without auth:
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    # FLAW (4)
    print("LOG: todo_deleted user=%s todo_id=%s" % (
                request.user.username if request.user.is_authenticated else 'none',
                todo_id))


    # FIX (4)
    # logger.info("todo_deleted user=%s todo_id=%s",
    #             request.user.username if request.user.is_authenticated else 'none',
    #             todo_id)

    return redirect('index')


def toggle(request, todo_id):
    # FIX (3)
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

    # FLAW (4)
    print("LOG: todo_toggled user=%s todo_id=%s done=%s" % (
                request.user.username if request.user.is_authenticated else 'none', 
                todo_id, 
                todo.done))

    # FIX (4)
    # logger.info("todo_toggled user=%s todo_id=%s done=%s", 
    #             request.user.username if request.user.is_authenticated else 'none', 
    #             todo_id, 
    #             todo.done)

    return redirect('index')
