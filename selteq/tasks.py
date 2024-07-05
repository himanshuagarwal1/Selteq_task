# tasks.py

from celery import shared_task
from selteq.models import Task
from django.utils import timezone

@shared_task
def print_task_details():
    tasks = Task.objects.filter(user_id=1)
    print("acknowledge")
    for task in tasks:
        print(f'Task: {task.title}, Duration: {task.duration}, Created At: {task.created_at}')
