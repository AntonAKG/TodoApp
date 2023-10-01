from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Todo, User

admin.site.register(Todo)

LogEntry._meta.get_field('user').related_model = User

admin.site.register(LogEntry)
