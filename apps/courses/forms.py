from django import forms
from courses.models import Lesson, Course, StudentAnswerLesson, Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('text', 'answer')

class StudentAnswerForm(forms.ModelForm):
    class Meta:
        model = StudentAnswerLesson
        fields = ('task', 'lesson', 'answer', 'student')
        widgets = {
            'task': forms.HiddenInput(),
            'lesson': forms.HiddenInput(),
            'student': forms.HiddenInput()
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'video', 'courses', 'tasks', 'type')

class CourseForm(forms.ModelForm):
    lessons = forms.ModelMultipleChoiceField(queryset=Lesson.objects.all())
    class Meta:
        model = Course
        fields = ('title', 'price')

