from django.shortcuts import render
from django.views.generic import ListView
from courses.models import Course



class ShowCourses(ListView):
    model = Course
    template_name = 'show_courses.html'
    context_object_name = 'courses'
