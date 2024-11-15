from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import Todo
from .serializers import TodoListSerializer, TodoDetailSerializer, TodoCreateSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.filter(complete=False)

    def get_serializer_class(self):
        if self.action == 'list':
            return TodoListSerializer
        elif self.action == 'retrieve':
            return TodoDetailSerializer
        return TodoCreateSerializer

class DoneTodoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Todo.objects.filter(complete=True)
    serializer_class = TodoListSerializer

    @action(detail=True, methods=['put'])
    def mark_done(self, request, pk=None):
        todo = get_object_or_404(Todo, id=pk)
        todo.complete = True
        todo.save()
        serializer = TodoListSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
