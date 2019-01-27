from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_app.index, name='todo_index'),
    path('addtodo', views.todo_app.addtodo, name='todo_addtodo'),
    path('deletetodo/<int:id>', views.todo_app.deletetodo, name='todo_deletetodo'),
]
