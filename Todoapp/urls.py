from .views import *
from django.urls import path


app_name = 'Todoapp'
urlpatterns = [
    path('api/v1/tasks/', TaskListCreateAPI.as_view(), name='tasks_list'),
    path('api/v1/tasks/<int:id>/', TaskDetailAPI.as_view(), name='task_detail')
]