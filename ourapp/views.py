from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User

from django.contrib.auth.models import Group
from .forms import CreatUserForm,ContentForm
from .forms import UserRegisterForm, StudentProfileForm, TeacherProfileForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from itertools import count, repeat,chain

from django.urls import reverse_lazy
from  .models import Content
from .models import User

from django.contrib.auth.decorators import login_required
from .models import Content
from .forms import ContentForm
from django.db import IntegrityError

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
import os


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
            return redirect('HomePage')
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Teacher').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('teacher_mainpage')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request, 'login_teacher.html', context)








def contact(request):
    return HttpResponse('contact Page')

def AdminLogIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('HomePageAdmin')  # Redirect to your home page or dashboard
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'AdminLogIn.html')


















def homeadmin(request):
    return render(request, 'HomePageAdmin.html')

def TeacherTable(request):
    return render(request, 'TeacherTable.html')

def studenttable(request):
    return render(request, 'StudentTable.html')

def AddContent(request, username):

    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.user = username  # Assign the correct User instance
            content.save()
            return redirect('ContentList')
    else:
        form = ContentForm()

    return render(request, 'AddContent.html', {'form': form})

# def check_database(request):
#     db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
#     db_exists = os.path.exists(db_path)
#     db_name = settings.DATABASES['default']['NAME']
#     users = User.objects.all()
#     user_list = ",".join([user.username for user in users])
#     return HttpResponse(f"Users: {user_list}, DB Path: {db_path}, DB Exists: {db_exists}, DB Name: {db_name}")
def ContentList(request,username):
    contents = Content.objects.filter(user=username)
    return render(request, 'ContentListTeacher.html', {'contents': contents})


def delete_Contant(request, pk,username):
    product = Content.objects.get(pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('ContentList' ,username)
    context = {'content': product}
    return render(request, 'DeleteContent.html', context)
def homestudent(request):
    return render(request, 'HomePageStudent.html')

def viewContent(request):
    soft = Content.objects.all()
    return render(request, 'viewContent.html', {'soft': soft})

def Review_teacher_list(request):
    teacher_group = Group.objects.get(name='Teacher')
    teachers = User.objects.filter(groups=teacher_group)

    return render(request, 'Review_teacher_list.html',{'teachers':teachers} )

def Review_Student_list(request):
    teacher_group = Group.objects.get(name='Student')
    teachers = User.objects.filter(groups=teacher_group)

    return render(request, 'Review_Student_list.html',{'teachers':teachers} )
