from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Todo

class BaseTodoTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.todo = Todo.objects.create(
            title="할 일 1",
            description="이것은 첫 번째 할 일입니다.",
            complete=False,
            important=True
        )

class TodoListViewTest(BaseTodoTest):
    def test_get_todo_list(self):
        response = self.client.get("/todo/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreater(len(response.data), 0)

    def test_create_todo(self):
        todo_data = {
            "title":"할 일 2",
            "description":"이것은 두 번째 할 일입니다.",
            "important":False,
        }
        response = self.client.post("/todo/", todo_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], todo_data["title"])

    def test_create_todo_invalid_data(self):
        invalid_data = {
            "title":"",
            "description":"이것은 유효하지 않은 할 일입니다.",
            "important":False,
        }
        response = self.client.post("/todo/", invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TodoViewTest(BaseTodoTest):
    def test_get_todo(self):
        response = self.client.get(f"/todo/{self.todo.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.todo.title)

    def test_put_todo(self):
        updated_data = {
            "title":"할 일 1 수정",
            "description":"이것은 수정된 할 일입니다.",
        }
        response = self.client.put(f"/todo/{self.todo.id}/", updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], updated_data["title"])
        self.assertEqual(response.data["description"], updated_data["description"])

class DoneTodoListTest(BaseTodoTest):
    def test_get_done_list(self):
        response = self.client.get("/todo/done/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_done_todo(self):
        response = self.client.get(f"/todo/{self.todo.id}/done/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["complete"], True)
