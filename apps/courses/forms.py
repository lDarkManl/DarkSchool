from django import forms
from courses.models import StudentAnswerLesson, StudentAnswerWebinar


class StudentAnswerForm(forms.ModelForm):
    class Meta:
        model = StudentAnswerLesson
        fields = ('task', 'lesson', 'answer')
        widgets = {
            'task': forms.HiddenInput(),
            'lesson': forms.HiddenInput()
        }
