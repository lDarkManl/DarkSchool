from django.contrib import admin
from courses.models import Course, Discipline, Lesson, StudentAnswerLesson, Task

admin.site.register(Course)
admin.site.register(Discipline)
admin.site.register(Lesson)
admin.site.register(StudentAnswerLesson)
admin.site.register(Task)