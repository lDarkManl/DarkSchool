from django.db import models
from accounts.models import StudentAccount

class Task(models.Model):
    discipline = models.ForeignKey(
        'courses.Discipline',
        on_delete=models.CASCADE,
        verbose_name='discipline',
        related_name='tasks'
    )
    text = models.TextField('Текст задачи')
    answer = models.TextField('Ответ на задачу')


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

    def __str__(self):
        return self.title

# Урок, в котором видео и дз
class Lesson(models.Model):
    title = models.CharField('Название урока', max_length=100)
    video = models.URLField('Ссылка на видео')
    courses = models.ManyToManyField(
        Course,
        blank=True,
        null=True,
        verbose_name='courses',
        related_name='lessons'
    )
    tasks = models.ManyToManyField(
        'courses.Task',
        blank=True,
        null=True,
        verbose_name='tasks',
        related_name='lessons'
    )
    is_lesson = models.BooleanField(default=False)
    is_webinar = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class StudentAnswerLesson(models.Model):
    answer = models.CharField('Ответ на задание', max_length=200, blank=True, null=True)
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name='lesson',
        related_name='answers'
    )
    task = models.ForeignKey(
        'courses.Task',
        on_delete=models.CASCADE,
        verbose_name='task',
        related_name='answers_lessons'
    )
    student = models.ForeignKey(
        StudentAccount,
        on_delete=models.CASCADE,
        verbose_name='student',
        related_name='answers_lessons'
    )

    def __str__(self):
        return self.answer

    def check_answer(self):
        return self.answer == self.task.answer

class Discipline(models.Model):
    title = models.CharField('Название предмета', max_length=100)

    def __str__(self):
        return self.title
