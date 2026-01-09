from django.urls import path
from . import views

urlpatterns = [
    path("", views.todos, name="todos"),  # GET = list, POST = create
    path("<int:id>/", views.todo_detail, name="todo"),
]
