from django.db import models

class TaskCategory(models.Model):
    category_name = models.CharField(max_length=200)
    tasks = models.ManyToManyField('task.TaskModel', related_name='categories')

    def __str__(self):
        return self.category_name
