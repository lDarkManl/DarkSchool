from django.shortcuts import render
from django.views.generic import ListView, DetailView
from courses.models import Course, Lesson


class ShowCourses(ListView):
    model = Course
    template_name = 'courses/show_courses.html'
    context_object_name = 'courses'


class ShowCourse(DetailView):
    model = Course
    template_name = 'courses/show_course.html'
    context_object_name = 'course'

class ShowLesson(DetailView):
    model = Lesson
    template_name = 'courses/show_lesson.html'
    context_object_name = 'lesson'

class ShowHomework(ListView):
    pass