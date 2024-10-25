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


# Абстрактный класс для занятия
class SchoolWork(models.Model):
    video = models.URLField('Ссылка на видео')

    class Meta:
        abstract = True


# Урок, в котором видео и дз
class Lesson(SchoolWork):
    title = models.CharField('Название урока', max_length=100)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='course',
        related_name='lessons'
    )
    tasks = models.ManyToManyField(
        'courses.Task',
        blank=True,
        null=True,
        verbose_name='tasks',
        related_name='lessons'
    )

    def __str__(self):
        return self.title


# Вебинар, в котором ссылка на стрим и дз
class Webinar(SchoolWork):
    title = models.CharField('Название вебинара', max_length=100)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='course',
        related_name='webinars'
    )
    tasks = models.ManyToManyField(
        'courses.Task',
        blank=True,
        null=True,
        verbose_name='tasks',
        related_name='webinars'
    )

    def __str__(self):
        return self.title


# Ответ ученика на конкретное задание в уроке
class StudentAnswer(models.Model):
    answer = models.CharField('Ответ на задание', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.answer

    def check_answer(self):
        return self.answer == self.task.answer

    class Meta:
        abstract = True


class StudentAnswerLesson(StudentAnswer):
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


class StudentAnswerWebinar(StudentAnswer):
    webinar = models.ForeignKey(
        Webinar,
        on_delete=models.CASCADE,
        verbose_name='webinar',
        related_name='answers'
    )
    task = models.ForeignKey(
        'courses.Task',
        on_delete=models.CASCADE,
        verbose_name='task',
        related_name='answers_webinars'
    )


class Discipline(models.Model):
    title = models.CharField('Название предмета', max_length=100)

    def __str__(self):
        return self.title
