from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.mixins import UserPassesTestMixin
from courses.models import Course, Lesson, StudentAnswerLesson
from courses.forms import StudentAnswerForm

def get_context_for_lesson(pk):
    lesson = Lesson.objects.get(pk=pk)
    context = {
        'lesson': lesson,
        'tasks': {task: StudentAnswerForm(initial={'task': task, 'lesson': lesson})
                  for task in lesson.tasks.all()},
    }
    return context

def save_answers(request):
    lesson = request.POST.get('lesson')
    answers = request.POST.getlist('answer')
    tasks = request.POST.getlist('task')
    for i in range(len(tasks)):
        form = StudentAnswerForm({'answer': answers[i], 'task': tasks[i], 'lesson': lesson, 'student': request.user.student})
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
