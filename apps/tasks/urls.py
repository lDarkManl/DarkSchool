from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
	path('task/<int:pk>/', views.TaskView.as_view(), name='task')
]