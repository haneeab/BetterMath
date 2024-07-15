from django.urls import path
from .views import register_student, register_teacher
from ourapp import views


urlpatterns = [

    path('register_student.html', views.register_student, name='register_student'),
    path('', views.home, name='home'),
    path('teacher_mainpage', views.teacher_mainpage, name='teacher_mainpage'),
    # path('register_teacher', views.register_teacher, name='register_teacher'),


]
