from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from courses.models import Course, Lesson, Task, StudentAnswerLesson
from courses import services
from courses.forms import LessonForm, CourseForm, TaskForm


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
        return render(request, 'courses/show_lesson.html', context)

    def post(self, request, pk):
        form = services.save_answers(request)
        if form:
            context = services.get_context_for_lesson(pk)
            return render(request, 'courses/show_lesson.html', context)
        return HttpResponseRedirect(reverse('courses:lesson', args=[pk]))


class CreateTask(services.TeacherRequiredMixin, LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'courses/create_task.html'

    def form_valid(self, form):
        form.instance.discipline = self.request.user.teacher.discipline
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks:task', args=[self.object.pk])

class CreateLesson(services.TeacherRequiredMixin, LoginRequiredMixin, CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'courses/create_lesson.html'

    def get_success_url(self):
        return reverse('courses:lesson', args=[self.object.pk])

class CreateCourse(services.TeacherRequiredMixin, LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/create_course.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.teacher = self.request.user.teacher
        self.object.discipline = self.request.user.teacher.discipline
        self.object.save()
        for lesson in form.cleaned_data['lessons']:
            lesson.courses.add(self.object)
            lesson.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('courses:course', args=[self.object.pk])

class TaskView(DetailView):
    model = Task
    template_name = 'courses/task.html'
    context_object_name = 'task'

class ShowHomeworkLesson(View):

    def get(self, request, pk):
        context = services.get_context_for_howework(request, pk)


