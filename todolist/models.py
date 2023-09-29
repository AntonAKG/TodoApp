from django.db import models


# Create your models here.


class Todo(models.Model):
    title = models.CharField(verbose_name='Назва задачі', max_length=500)
    is_complete = models.BooleanField(verbose_name='Закінчено', default=False)

    class Meta:
        verbose_name = "Задачі"
        verbose_name_plural = 'Задачі'

    def __str__(self):
        return self.title
