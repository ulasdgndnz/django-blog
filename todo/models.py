from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_title = models.CharField(max_length=25, verbose_name="Başlık")
    checked = models.BooleanField(verbose_name="Durum")

    def __str__(self):
        return self.todo_title
