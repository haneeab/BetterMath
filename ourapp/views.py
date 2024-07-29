from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

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
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm,QuizForm
from .models import Profile
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
            messages.success(request, 'Account was created for {username}')
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

@login_required
def teacher_mainpage (request):
    return render(request,'teacher_mainpage.html')

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

from django.shortcuts import render, redirect
from .forms import ContentForm
from .models import User

def AddContent(request, username):
    error_message = None
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            unit = form.cleaned_data.get('unit')
            if unit not in [3, 4, 5]:
                error_message = "Unit must be 3, 4, or 5."
            else:
                content = form.save(commit=False)
                content.user = username  # Correct User instance assignment
                content.save()
                return redirect('ContentList', username)
    else:
        form = ContentForm()

    return render(request, 'AddContent.html', {'form': form, 'error_message': error_message})


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


def addstudent(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HomePage')

    conaxt = {'form': form}
    return render(request, 'addstudent.html', conaxt)


def logoutl(request):
    logout(request)
    return redirect('HomePage')

def Review_teacher_list(request):
    users_in_group = Group.objects.get(name='Teacher').user_set.all()

    teacher_group = Group.objects.get(name='Teacher')
    teachers = User.objects.filter(groups=teacher_group)
    context = {'users_in_group': users_in_group}
    return render(request, 'Review_teacher_list.html', {'users_in_group': users_in_group})

def Review_Student_list(request):
    users_in_group = Group.objects.get(name='Student').user_set.all()

    teacher_group = Group.objects.get(name='Student')
    teachers = User.objects.filter(groups=teacher_group)

    return render(request, 'Review_Student_list.html', {'users_in_group': users_in_group})



def edit_profile(request,username):
    # Get or create the profile based on the username
    profile, created = Profile.objects.get_or_create(user=username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('HomePageStudent')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'EditProfileStudent.html', context)
def edit_profile_Teacher(request,username):
    # Get or create the profile based on the username
    profile, created = Profile.objects.get_or_create(user=username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('teacher_mainpage')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'EditProfileTeacher.html', context)


def Update_Content(request, pk, username):
    content = Content.objects.get(pk=pk)
    error_message = None
    if request.method == 'POST':
        form = ContentForm(request.POST, instance=content)
        if form.is_valid():
            unit = form.cleaned_data.get('unit')
            if unit not in [3, 4, 5]:
                error_message = "Unit must be 3, 4, or 5."
            else:
                form.save()
                return redirect('ContentList', username)
    else:
        form = ContentForm(instance=content)

    return render(request, 'UpdateContent.html', {'form': form, 'error_message': error_message})

def StudentLogIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Student').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('HomePageStudent')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request, 'StudentLogIn.html', context)


def AddTeacher(request):
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            try:
                group = Group.objects.get(name='Teacher')
            except ObjectDoesNotExist:
                group = None
            if group:
                user.groups.add(group)
            messages.success(request, 'Account was created for' ,{username})
            return redirect('Review_teacher_list')
    else:
        form = CreatUserForm()
    context = {'form': form}
    return render(request, 'AddTeacher.html', context)


from django.shortcuts import render, redirect
from .forms import QuizForm

def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user.username
            form.save()
            return redirect('teacher_mainpage')
        else:
            print("Debug: form.errors =", {form.errors})  # Debug statement
    else:
        form = QuizForm()

    return render(request, 'AddQuizTeacher.html', {'form': form})
def combined_list_3uints(request):
    contents = Content.objects.filter(unit=3)
    quizzes = Quiz.objects.filter(unit=3)
    return render(request, 'Math3Units.html', {'contents': contents, 'quizzes': quizzes})
def combined_list_4uints(request):
    contents = Content.objects.filter(unit=4)
    quizzes = Quiz.objects.filter(unit=4)
    return render(request, 'Math4Units.html', {'contents': contents, 'quizzes': quizzes})
def combined_list_5uints(request):
    contents = Content.objects.filter(unit=5)
    quizzes = Quiz.objects.filter(unit=5)
    return render(request, 'Math5Units.html', {'contents': contents, 'quizzes': quizzes})

def DeleteStudent(request, username):
    student  = User.objects.get(username=username)
    if request.method == 'POST':
        student.delete()
        return redirect('Review_Student_list')
    context = {'student': student}
    return render(request, 'DeleteStudent.html', context)

def delete_Contant(request, pk,username):
    product = Content.objects.get(pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('ContentList' ,username)
    context = {'content': product}
    return render(request, 'DeleteContent.html', context)