from django.urls import path
from .views import register_student, register_teacher
from ourapp import views

urlpatterns = [

    path('register_student.html', views.register_student, name='register_student'),
    path('', views.home),

    # path('register_teacher.html', views.register_teacher, name='register_teacher'),








   path('HomePageAdmin.html', views.homeadmin, name='HomePageAdmin'),
    path('TeacherTable.html', views.TeacherTable, name='TeacherTable'),
    path('StudentTable.html', views.studenttable, name='StudentTable'),

]
