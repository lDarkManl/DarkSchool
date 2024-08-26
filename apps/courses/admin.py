from django.contrib import admin
from courses.models import Course, Discipline, Lesson, Webinar

admin.site.register(Course)
admin.site.register(Discipline)
admin.site.register(Lesson)
admin.site.register(Webinar)