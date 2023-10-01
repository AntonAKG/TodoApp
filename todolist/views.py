from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from .forms import RegisterForm, LoginForm
from .models import Todo, User


class Index(View):
    template_name = 'main_menu/main.html'

    def get(self, request):
        context = {
            'title': 'Головна сторінка'
        }

        return render(request, template_name=self.template_name, context=context)


class Home(ListView):
    template_name = 'todoapp/task_list.html'
    model = User
    context_object_name = 'todo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_id = self.request.user.id
        context['todo'] = Todo.objects.filter(user_task=user_id)
        context['user'] = User.objects.get(id=user_id)

        return context


@method_decorator(login_required, name='dispatch')
class AddTodoView(View):
    def post(self, request):
        title = request.POST.get('title')
        if title:
            todo = Todo.objects.create(title=title, user_task_id=request.user.id)
        return redirect('home')

@method_decorator(login_required, name='dispatch')
class TodoUpdateView(View):
    def get(self, request, todo_id):
        todo = Todo.objects.get(id=todo_id)
        todo.is_complete = not todo.is_complete
        todo.save()
        return redirect('home')

@method_decorator(login_required, name='dispatch')
class TodoDeleteView(View):
    def get(self, request, todo_id):
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('home')


class Register(View):
    template_name = r'registration\register.html'

    def get(self, request):
        context = {
            'form': RegisterForm()
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(password=password, email=email)
            # login(request, user)
            return redirect('login')

        context = {
            'form': form
        }

        return render(request, self.template_name, context=context)


class LoginClassView(LoginView):
    LoginView.authentication_form = LoginForm
