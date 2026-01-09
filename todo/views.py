from django.http import JsonResponse
from .models import Todo
# from django.core import serializers


def todos(request):
    # return HttpResponse("Todo List")

    if request.method == "POST":
        todo = Todo.objects.create(title="hello world")
        return JsonResponse(todo_to_dict(todo))

    todos = Todo.objects.all().order_by("-created_at")
    return JsonResponse([todo_to_dict(todo) for todo in todos], safe=False)


def todo_detail(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == "PUT":
        todo.title = "hello Django"
        todo.completed = True
        todo.save()
        return JsonResponse(todo_to_dict(todo))

    if request.method == "DELETE":
        todo.delete()
        return JsonResponse({"success": True})

    return JsonResponse(todo_to_dict(todo))


def todo_to_dict(todo):
    return {
        "id": todo.id,
        "title": todo.title,
        "completed": todo.completed,
        "created_at": todo.created_at,
    }
