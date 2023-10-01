from django.contrib.auth.views import LoginView
from django.urls import path, include

from .forms import LoginForm
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('home', Home.as_view(), name='home'),
    path('add', AddTodoView.as_view(), name='add'),
    path('update/<int:todo_id>/', TodoUpdateView.as_view(), name='update'),
    path('delete/<int:todo_id>/', TodoDeleteView.as_view(), name='delete'),

    # '''Login and Register urls'''

    path('', include('django.contrib.auth.urls')),
    path('login/', LoginClassView.as_view(), name='login'),
    path('register/', Register.as_view(), name='register')

]
