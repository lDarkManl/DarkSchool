from django.db import models


class Task(models.Model):
    discipline = models.ForeignKey(
        'courses.Discipline',
        on_delete=models.CASCADE,
        verbose_name='discipline',
        related_name='tasks'
    )
    text = models.TextField('Текст задачи')
    answer = models.TextField('Ответ на задачу')
