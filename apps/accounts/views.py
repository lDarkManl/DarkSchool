from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.services import student_required, teacher_required
from accounts.models import User
from accounts.forms import StudentSignUpForm, TeacherSignUpForm, LoginForm

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/student_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student-home')

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'accounts/teacher_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teacher-home')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_student:
                return reverse('student-home')
            elif user.is_teacher:
                return reverse('teacher-home')
        else:
            return reverse('login')

@login_required
@student_required
def student_home(request):
    context = {
        'student': request.user.student,
    }
    return render(request, 'accounts/student_home.html', context)

@login_required
@teacher_required
def teacher_home(request):
    context = {
        'teacher': request.user.teacher,
    }
    return render(request, 'accounts/teacher_home.html', context)