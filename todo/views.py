from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from drf_yasg.utils import swagger_auto_schema

from .models import Todo
from .serializers import TodoListSerializer, TodoDetailSerializer, TodoCreateSerializer

class TodoListAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete=False)
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TodoCreateSerializer)
    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoAPIView(APIView):
    def get(self, request, id):
        todo = get_object_or_404(Todo, id=id)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TodoCreateSerializer)
    def put(self, request, id):
        todo = get_object_or_404(Todo, id=id)
        serializer = TodoCreateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoneTodoListAPIView(APIView): # 완료 목룍
    def get(self, request):
        dones = Todo.objects.filter(complete=True)
        serializer = TodoListSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DoneTodoAPIView(APIView): # 완료 설정
    def get(self, request, id):
        done = get_object_or_404(Todo, id=id)
        done.complete = True
        done.save()
        serializer = TodoDetailSerializer(done)
        return Response(serializer.data, status=status.HTTP_200_OK)

