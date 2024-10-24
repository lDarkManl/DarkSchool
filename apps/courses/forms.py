from django import forms
from courses.models import Lesson, Course, StudentAnswerLesson, StudentAnswerWebinar


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
        fields = ('title', 'course', 'tasks')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'price')