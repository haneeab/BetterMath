from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegisterForm, StudentProfileForm, TeacherProfileForm
from .models import User




def register_student(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        student_form = StudentProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.is_student = True
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            messages.success(request, 'Account created successfully for student!')
            login(request, user)
            return redirect('home')  # Redirect to a home page or student dashboard
    else:
        user_form = UserRegisterForm()
        student_form = StudentProfileForm()
    return render(request, 'register_student.html', {'user_form': user_form, 'student_form': student_form})

def register_teacher(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        teacher_form = TeacherProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save(commit=False)
            user.is_teacher = True
            user.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            messages.success(request, 'Account created successfully for teacher!')
            login(request, user)
            return redirect('home')  # Redirect to a home page or teacher dashboard
    else:
        user_form = UserRegisterForm()
        teacher_form = TeacherProfileForm()
    return render(request, 'register_teacher.html', {'user_form': user_form, 'teacher_form': teacher_form})
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'HomePage.html')








def contact(request):
    return HttpResponse('contact Page')

















def homeadmin(request):
    return render(request, 'HomePageAdmin.html')

def TeacherTable(request):
    return render(request, 'TeacherTable.html')

def studenttable(request):
    return render(request, 'StudentTable.html')
