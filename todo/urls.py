from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, DoneTodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')
router.register(r'done-todos', DoneTodoViewSet, basename='done-todo')

urlpatterns = [
    path('', include(router.urls)),
]
