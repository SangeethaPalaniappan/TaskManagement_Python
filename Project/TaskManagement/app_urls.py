from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_user, name='Users'),
    path(':<int:user_id>/tasks/', views.task_creation_updation, name='Task'),
    path(':<int:user_id>/tasks/:<int:task_id>/', views.update_task, name = 'task update'),
]