from django.db import models
from django.shortcuts import reverse


class Task(models.Model):
    tasks_title = models.CharField(max_length=255)
    due_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.tasks_title


    def get_detail_url(self):
        return reverse('tasks:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('tasks:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('tasks:delete', args=[self.pk])