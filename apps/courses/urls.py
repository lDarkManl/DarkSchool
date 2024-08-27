from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
	path('', views.ShowCourses.as_view(), name='courses'),
	path('course/<int:pk>', views.ShowCourse.as_view(), name='course'),
	path('lesson/<int:pk>', views.ShowLesson.as_view(), name='lesson'),
	path('homework/<int:pk>', views.ShowHomework.as_view(), name='homework')
]