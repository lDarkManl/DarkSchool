from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.mixins import UserPassesTestMixin
from courses.models import Course, Lesson, StudentAnswerLesson
from courses.forms import StudentAnswerForm

def get_context_for_lesson(pk):
    lesson = Lesson.objects.get(pk=pk)
    context = {
        'schoolwork': schoolwork,
        'tasks': {task: form_class(initial={'task': task, 'lesson': schoolwork})
                  for task in schoolwork.tasks.all()},
    }
    return context

def get_context_for_lesson(pk):
    context = get_context_for_schoolwork(pk, Lesson)
    return context

def get_context_for_webinar(pk):
    context = get_context_for_schoolwork(pk, Webinar)
    return context

def get_schoolwork_info(request):
    schoolwork = request.POST.get('lesson')
    if schoolwork is None:
        schoolwork = request.POST.get('webinar')
        schoolwork_title = 'webinar'
        form = StudentAnswerWebinarForm
    else:
        schoolwork_title = 'lesson'
        form = StudentAnswerLessonForm
    return schoolwork_title, schoolwork, form


def save_answers(request):
    schoolwork_title, schoolwork, form_class = get_schoolwork_info(request)
    answers = request.POST.getlist('answer')
    tasks = request.POST.getlist('task')
    print(request.user.student)
    for i in range(len(tasks)):
        form = form_class({'answer': answers[i], 'task': tasks[i], schoolwork_title: schoolwork, 'student': request.user.student})
        if form.is_valid():
            form.save()
        else:
            return form
    return None

def get_context_for_homework(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    answers = StudentAnswerLesson.objects.filter(student=request.user.student, lesson=lesson)
    tasks = lesson.tasks.all()
    context = {
        'tasks': tasks,
        'answers': answers
    }

class StudentRequiredMixin(UserPassesTestMixin):
    login_url = 'accounts:login'

    def test_func(self):
        self.test_func = lambda u: u.is_active and u.is_student

class TeacherRequiredMixin(UserPassesTestMixin):
    login_url = 'accounts:login'

    def test_func(self):
        return self.request.user.is_teacher
