from django.urls import path
from .views import register_student, register_teacher
from ourapp import views

urlpatterns = [

    path('register_student.html', views.register_student, name='register_student'),
    path('', views.home, name='HomePage'),
    path('AdminLogIn', views.AdminLogIn, name='AdminLogIn')

    # path('register_teacher.html', views.register_teacher, name='register_teacher'),

]
