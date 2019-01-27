from django.shortcuts import render, HttpResponse, redirect

from .models import Todo
# Create your views here.

class todo_app:

    def index(request):
        todos = Todo.objects.all()

        return render(request,"todo/todos.html", {"todos":todos})

    def addtodo(request):
        todo = Todo()
        todo.checked = False
        todo.todo_title = request.POST.get("todotitile")
        todo.save()


        return redirect("/todos/")

    def deletetodo(request, id):
        todo = Todo.objects.get(id=id)
        todo.delete()

        return redirect("/todos/")
