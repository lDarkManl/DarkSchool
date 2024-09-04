from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponseRedirect

from courses.models import Course, Lesson
from courses import services


class ShowCourses(ListView):
    model = Course
    template_name = 'courses/show_courses.html'
    context_object_name = 'courses'


class ShowCourse(DetailView):
    model = Course
    template_name = 'courses/show_course.html'
    context_object_name = 'course'


class ShowLesson(View):

    def get(self, request, pk):
        context = services.get_context_for_lesson(pk)
        return render(request, 'courses/show_schoolwork.html', context)

    def post(self, request, pk):
        form = services.save_answers(request)
        if form:
            context = services.get_context_for_lesson(pk)
            return render(request, 'courses/show_schoolwork.html', context)
        return HttpResponseRedirect(reverse('courses:lesson', args=[pk]))


class ShowWebinar(View):

    def get(self, request, pk):
        context = services.get_context_for_webinar(pk)
        return render(request, 'courses/show_schoolwork.html', context)

    def post(self, request, pk):
        form = services.save_answers(request)
        if form:
            context = services.get_context_for_webinar(pk)
            return render(request, 'courses/show_schoolwork.html', context)
        return HttpResponseRedirect(reverse('courses:webinar', args=[pk]))
