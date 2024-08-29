from courses.models import Course, Lesson, Webinar
from courses.forms import StudentAnswerForm


def get_context_for_lesson(pk):
    lesson = Lesson.objects.get(pk=pk)
    context = {
        'lesson': lesson,
        'tasks': {task: StudentAnswerForm(initial={'task': task, 'lesson': lesson})
                  for task in lesson.tasks.all()}
    }
    return context


def save_answers(request):
    lesson = request.POST.get('lesson')
    answers = request.POST.getlist('answer')
    tasks = request.POST.getlist('task')
    for i in range(len(answers)):
        form = StudentAnswerForm({'answer': answers[i], 'task': tasks[i], 'lesson': lesson})
        if form.is_valid():
            form.save()
        else:
            return form
    return None
