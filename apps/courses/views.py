from django.shortcuts import render
from django.views.generic import ListView, DetailView
from courses.models import Course


class ShowCourses(ListView):
    model = Course
    template_name = 'courses/show_courses.html'
    context_object_name = 'courses'


class ShowCourse(DetailView):
    model = Course
    template_name = 'courses/show_course.html'
    context_object_name = 'course'
