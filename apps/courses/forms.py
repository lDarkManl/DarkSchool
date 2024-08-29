from django import forms
from courses.models import StudentAnswer


class StudentAnswerForm(forms.ModelForm):
    class Meta:
        model = StudentAnswer
        fields = ('task', 'lesson', 'answer')
        widgets = {
            'task': forms.HiddenInput(),
            'lesson': forms.HiddenInput()
        }
