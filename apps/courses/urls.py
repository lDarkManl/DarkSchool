from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
	path('', views.ShowCourses.as_view(), name='courses'),
	path('course/<int:pk>', views.ShowCourse.as_view(), name='course'),
	path('lesson/<int:pk>', views.ShowLesson.as_view(), name='lesson'),
	path('webinar/<int:pk>', views.ShowWebinar.as_view(), name='webinar'),
	path('create_task/', views.CreateTask.as_view(), name='create_task'),
	path('create_lesson/', views.CreateLesson.as_view(), name='create_lesson'),
	path('create_course/', views.CreateCourse.as_view(), name='create_course'),
]