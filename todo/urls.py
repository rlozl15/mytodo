from django.urls import path, include
from .views import TodoListAPIView, TodoAPIView, DoneTodoListAPIView, DoneTodoAPIView

urlpatterns = [
    path("", TodoListAPIView.as_view()),
    path("<int:id>/", TodoAPIView.as_view()),
    path("<int:id>/done/", DoneTodoAPIView.as_view()),
    path("done/", DoneTodoListAPIView.as_view()),
]
