from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class TeacherAccount(models.Model):
    name = models.CharField('Имя', max_length=100)
    age = models.IntegerField('Возраст')
    info = models.TextField('Информация о человеке')
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='user',
        related_name='teacher'
    )
    discipline = models.ForeignKey(
        'courses.Discipline',
        on_delete=models.CASCADE,
        verbose_name='discipline',
        related_name='teachers'
    )

    def __str__(self):
        return self.name


class StudentAccount(models.Model):
    name = models.CharField('Имя', max_length=100)
    age = models.IntegerField('Возраст')
    info = models.TextField('Информация о человеке')
    details = models.TextField('Реквизиты для оплаты')
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='user',
        related_name='student',
    )
    courses = models.ManyToManyField(
        'courses.Course',
        blank=True,
        null=True,
        verbose_name='courses',
        related_name='students'
    )

    def __str__(self):
        return self.name