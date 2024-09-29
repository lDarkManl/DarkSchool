from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('teacher_home', views.teacher_home, name='teacher_home'),
    path('student_home', views.student_home, name='student_home'),
    path('teacher_signup', views.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('student_signup', views.StudentSignUpView.as_view(), name='student_signup'),
]