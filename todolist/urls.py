from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('add', AddTodoView.as_view(), name='add'),
    path('update/<int:todo_id>/', TodoUpdateView.as_view(), name='update'),
    path('delete/<int:todo_id>/', TodoDeleteView.as_view(), name='delete'),
]