from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from django import forms
from django.contrib.auth import get_user_model
from accounts.models import User, StudentAccount, TeacherAccount
from courses.models import Discipline


class StudentSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    age = forms.IntegerField()
    info = forms.CharField(widget=forms.Textarea())
    details = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = User
        fields = ('username', 'age', 'info', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        student = StudentAccount.objects.create(
            user=user,
            name=self.cleaned_data.get('username'),
            age=self.cleaned_data.get('age'),
            info=self.cleaned_data.get('info'),
            details=self.cleaned_data.get('details'),
        )
        return user


class TeacherSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    age = forms.IntegerField()
    info = forms.CharField(widget=forms.Textarea())
    discipline = forms.ModelChoiceField(queryset=Discipline.objects.all(), empty_label=None)

    class Meta:
        model = User
        fields = ('username', 'age', 'info', 'password1', 'password2', 'discipline')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        teacher = TeacherAccount.objects.create(
            user=user,
            name=self.cleaned_data.get('username'),
            age=self.cleaned_data.get('age'),
            info=self.cleaned_data.get('info'),
            discipline=self.cleaned_data.get('discipline')
        )
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
