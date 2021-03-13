from django.urls import path
from . import views

urlpatterns = [
    path('',views.CreateTaskView.as_view()),
    path('task/<int:pk>/',views.TaskView.as_view()),
    path('get-project-fields',views.get_project_fields),
    path('task-date-range',views.tasks_by_date),
]