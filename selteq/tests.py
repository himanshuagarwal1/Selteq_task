from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from .models import Task
from django.contrib.auth.models import User
from datetime import timedelta

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)        
        self.task = Task.objects.create(user=self.user, title='Test Task', duration=timedelta(60))
    

    def test_create_task(self):
        response = self.client.post("/task/create/", {'title': 'New Task', 'duration': 30})
      
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_list_tasks(self):
        response = self.client.get('/task/list/')        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_task(self):
        response = self.client.get(f'/task/retrieve/{self.task.id}/')       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_task(self):
        response = self.client.put(f'/task/update/{self.task.id}/', {'title': 'Updated Task'})        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_delete_task(self):
        response = self.client.delete(f'/task/delete/{self.task.id}/')       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 0)
