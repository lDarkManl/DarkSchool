from courses.models import Course, Lesson, Webinar
from courses.forms import StudentAnswerForm

def get_context_for_schoolwork(pk, model):
    schoolwork = model.objects.get(pk=pk)
    context = {
        'schoolwork': schoolwork,
        'tasks': {task: StudentAnswerForm(initial={'task': task, 'schoolwork': schoolwork})
                  for task in schoolwork.tasks.all()},
    }
    return context

def get_context_for_lesson(pk):
    context = get_context_for_schoolwork(pk, Lesson)
    return context

def get_context_for_webinar(pk):
    context = get_context_for_schoolwork(pk, Webinar)
    return context

def save_answers(request):
    schoolwork = request.POST.get('schoolwork')
    answers = request.POST.getlist('answer')
    tasks = request.POST.getlist('task')
    for i in range(len(answers)):
        form = StudentAnswerForm({'answer': answers[i], 'task': tasks[i], 'schoolwork': schoolwork})
        if form.is_valid():
            form.save()
        else:
            return form
    return None
