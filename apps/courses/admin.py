from django.contrib import admin
from courses.models import Course, Discipline, Lesson, Webinar, StudentAnswerLesson, StudentAnswerWebinar, Task

admin.site.register(Course)
admin.site.register(Discipline)
admin.site.register(Lesson)
admin.site.register(Webinar)
admin.site.register(StudentAnswerLesson)
admin.site.register(StudentAnswerWebinar)
admin.site.register(Task)