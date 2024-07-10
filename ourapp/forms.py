from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User , Student ,Teacher

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
