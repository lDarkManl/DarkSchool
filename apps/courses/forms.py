from django import forms
from courses.models import Lesson, Webinar, Course, StudentAnswerLesson, StudentAnswerWebinar, Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('text', 'answer')

class StudentAnswerForm(forms.ModelForm):
    class Meta:
        model = StudentAnswerLesson
        fields = ('task', 'lesson', 'answer')
        widgets = {
            'task': forms.HiddenInput(),
            'lesson': forms.HiddenInput()
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'video', 'courses', 'tasks')

class CourseForm(forms.ModelForm):
    lessons = forms.ModelMultipleChoiceField(queryset=Lesson.objects.all())
    class Meta:
        model = Course
        fields = ('title', 'price')

class WebinarForm(forms.ModelForm):
    class Meta:
        model = Webinar
        fields = ('title', 'video', 'courses', 'tasks')