from django.db import models


class Account(models.Model):
    name = models.CharField('Имя', max_length=100)
    age = models.IntegerField('Возраст')
    info = models.TextField('Информация о человеке')

    class Meta:
        abstract = True


class TeacherAccount(Account):
    discipline = models.ForeignKey(
        'courses.Discipline',
        on_delete=models.CASCADE,
        verbose_name='discipline',
        related_name='teachers'
    )


class StudentAccount(Account):
    details = models.TextField('Реквизиты для оплаты')
    courses = models.ManyToManyField(
        'courses.Course',
        blank=True,
        null=True,
        verbose_name='courses',
        related_name='students'
    )
