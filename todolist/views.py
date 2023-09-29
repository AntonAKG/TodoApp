from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from .models import Todo


class Index(ListView):
    model = Todo
    context_object_name = 'article'
    template_name = 'todoapp/index.html'


class AddTodoView(View):
    @method_decorator(require_http_methods(['POST']))
    def post(self, request):
        title = request.POST.get('title')
        if title:
            todo = Todo.objects.create(title=title)
        return redirect('index')


class TodoUpdateView(View):
    def get(self, request, todo_id):
        todo = Todo.objects.get(id=todo_id)
        todo.is_complete = not todo.is_complete
        todo.save()
        return redirect('index')


class TodoDeleteView(View):
    def get(self, request, todo_id):
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('index')
