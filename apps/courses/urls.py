from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
	path('', views.ShowCourses.as_view(), name='courses'),
	path('<int:pk>', views.ShowCourse.as_view(), name='course')
]