from app.views import TodoListAndCreate, TodoChangeDelete
from django.urls import path

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoChangeDelete.as_view()),
]
