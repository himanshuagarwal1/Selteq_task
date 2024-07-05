# myapp/management/commands/print_tasks.py

import time
from django.core.management.base import BaseCommand
from selteq.models import Task

class Command(BaseCommand):
    help = 'Prints all tasks in the database one by one after every 10 seconds'

    def handle(self, *args, **kwargs):
        tasks = Task.objects.all()
        for task in tasks:
            self.stdout.write(f'Task ID: {task.id}, Title: {task.title}')
            time.sleep(10)
