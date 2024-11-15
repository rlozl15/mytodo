from rest_framework import serializers
from .models import Todo


class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        exclude = ['description','created'] # 제외 필드 설정

class TodoDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(help_text="pk")
    class Meta:
        model = Todo
        fields = '__all__'

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title','description','important']

