from django.urls import path
from .views import register_student, register_teacher ,AddContent,check_database
from ourapp import views


urlpatterns = [

    path('register_student.html', views.register_student, name='register_student'),
    path('', views.home, name='home'),
    path('teacher_mainpage', views.teacher_mainpage, name='teacher_mainpage'),
    # path('register_teacher', views.register_teacher, name='register_teacher'),

    path('', views.home, name='HomePage'),
    path('AdminLogIn', views.AdminLogIn, name='AdminLogIn'),
    path('login_teacher/', views.login_teacher,name='TeacherLogIn'),

    # path('register_teacher.html', views.register_teacher, name='register_teacher'),

    path('HomePageAdmin.html', views.homeadmin, name='HomePageAdmin'),
    path('TeacherTable.html', views.TeacherTable, name='TeacherTable'),
    path('StudentTable.html', views.studenttable, name='StudentTable'),
    path('AddContent/<str:username>/', views.AddContent, name="AddContent"),
    path('check-database/',views.check_database,name="check_database"),
    path('ContentList/<str:username>/', views.ContentList, name='ContentList'),
    path('content/<int:pk>/<str:username>/', views.delete_Contant, name='delete_content'),

]
