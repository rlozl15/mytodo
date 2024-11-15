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

class TodoViewSetTest(BaseTodoTest):
    def test_get_todo_list(self):
        response = self.client.get("/todo/todos/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreater(len(response.data), 0)

    def test_create_todo(self):
        todo_data = {
            "title": "할 일 2",
            "description": "이것은 두 번째 할 일입니다.",
            "important": False,
        }
        response = self.client.post("/todo/todos/", todo_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], todo_data["title"])

    def test_create_todo_invalid_data(self):
        invalid_data = {
            "title": "",
            "description": "이것은 유효하지 않은 할 일입니다.",
            "important": False,
        }
        response = self.client.post("/todo/todos/", invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_single_todo(self):
        response = self.client.get(f"/todo/todos/{self.todo.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.todo.title)

    def test_update_todo(self):
        updated_data = {
            "title": "할 일 1 수정",
            "description": "이것은 수정된 할 일입니다.",
            "important": True,
        }
        response = self.client.put(f"/todo/todos/{self.todo.id}/", updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], updated_data["title"])
        self.assertEqual(response.data["description"], updated_data["description"])

    def test_delete_todo(self):
        response = self.client.delete(f"/todo/todos/{self.todo.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Todo.objects.filter(id=self.todo.id).exists())


class DoneTodoViewSetTest(BaseTodoTest):
    def test_get_done_todo_list(self):
        self.todo.complete = True
        self.todo.save()
        response = self.client.get("/todo/done-todos/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)

    def test_mark_done(self):
        self.assertFalse(self.todo.complete)
        response = self.client.put(f"/todo/done-todos/{self.todo.id}/mark_done/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["complete"], True)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.complete)

    def test_mark_done_invalid_todo(self):
        response = self.client.put("/todo/done-todos/999999/mark_done/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)