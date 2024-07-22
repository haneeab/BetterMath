from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User , Student ,Teacher,Content
from .models import Profile


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile_picture', 'date_of_birth']

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['profile_picture', 'date_of_birth']
class CreatUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'description', 'unit']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']