from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
	path('', views.ShowCourses.as_view(), name='courses'),
]