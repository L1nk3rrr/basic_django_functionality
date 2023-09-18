from django.urls import path
from . import views

urlpatterns = [
    path('teacher-list/', views.teacher_list, name='teacher_list'),
]
