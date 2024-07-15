from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import CreatUserForm
from .forms import UserRegisterForm, StudentProfileForm, TeacherProfileForm
from django.contrib.auth import authenticate, login,logout

from .models import User




def register_student(request):
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            try:
                group = Group.objects.get(name='Student')
            except ObjectDoesNotExist:
                group = None
            if group:
                user.groups.add(group)
            messages.success(request, f'Account was created for {username}')
            return redirect('home')
    else:
        form = CreatUserForm()
    context = {'form': form}
    return render(request, 'register_student.html', context)


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
def teacher_mainpage (request):
    return  render( request,'teacher_mainpage.html')

def login_teacher(request):
    return render(request, 'login_teacher.html')






def contact(request):
    return HttpResponse('contact Page')

def AdminLogIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('HomePage')  # Redirect to your home page or dashboard
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'AdminLogIn.html')


















def homeadmin(request):
    return render(request, 'HomePageAdmin.html')

def TeacherTable(request):
    return render(request, 'TeacherTable.html')

def studenttable(request):
    return render(request, 'StudentTable.html')
