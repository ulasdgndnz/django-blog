from django.contrib import admin
from todo.models import Todo

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["todo_title", "checked"]

    class Meta:
        model = Todo
