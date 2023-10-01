from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Redefined User model add field like
    """
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Todo(models.Model):
    title = models.CharField(verbose_name='Назва задачі', max_length=500)
    is_complete = models.BooleanField(verbose_name='Закінчено', default=False)
    user_task = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Задачі"
        verbose_name_plural = 'Задачі'

    def __str__(self):
        return self.title
