from django.db import models


class Course(models.Model):
    title = models.CharField('Название курса', max_length=100)
    price = models.IntegerField('Цена курса')
    teacher = models.ForeignKey(
        'accounts.TeacherAccount',
        on_delete=models.CASCADE,
        verbose_name='teacher',
        related_name='teacher_accounts'
    )
    discipline = models.ForeignKey(
        'Discipline',
        on_delete=models.CASCADE,
        verbose_name='discipline',
        related_name='courses'
    )

    class Meta:
        app_label = 'courses'


# Абстрактный класс для занятия
class SchoolWork(models.Model):
    video = models.URLField('Ссылка на видео')
    tasks = models.ManyToManyField(
        'tasks.Task',
        blank=True,
        null=True,
        verbose_name='tasks',
        related_name='schoolworks'
    )


# Урок, в котором видео и дз
class Lesson(SchoolWork):
    title = models.CharField('Название урока', max_length=100)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='course',
        related_name='lessons'
    )


# Вебинар, в котором ссылка на стрим и дз
class Webinar(SchoolWork):
    title = models.CharField('Название вебинара', max_length=100)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='course',
        related_name='webinars'
    )


# Домашнее задание конкретного ученика
class StudentHomeWork(models.Model):
    student = models.ForeignKey(
        'accounts.StudentAccount',
        on_delete=models.CASCADE,
        verbose_name='student',
        related_name='homeworks'
    )
    tasks = models.ManyToManyField(
        'tasks.Task',
        blank=True,
        null=True,
        verbose_name='tasks',
        related_name='homeworks'
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name='lesson',
        related_name='homework'
    )


class Discipline(models.Model):
    title = models.CharField('Название предмета', max_length=100)
