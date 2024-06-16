from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_user, name='Users'),
    path(':<int:user_id>/task/', views.create_task, name='Users'),
]