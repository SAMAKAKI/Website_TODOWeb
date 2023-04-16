from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('todo/', TODOView.as_view(), name='todo'),
    path('todo/<id>', TODOTasksView.as_view(), name='todo-tasks'),
    path('todo/create-project/', CreateProjectView.as_view(), name='create-project'),
    path('todo/create-task/', CreateTaskView.as_view(), name='create-task'),
    path('todo/task-is-done/', is_done, name='is-done'),
]
