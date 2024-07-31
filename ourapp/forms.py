from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User , Student ,Teacher,Content,Quiz
from .models import Profile
import json  # Import the json module

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


from django import forms
from .models import Quiz
import json


class QuizForm(forms.ModelForm):
    questions = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Quiz
        fields = ['name', 'user', 'questions','unit']

    def clean_questions(self):
        questions_data = self.cleaned_data['questions']
        errors = []
        try:
            questions = json.loads(questions_data)
        except json.JSONDecodeError:
            errors.append('Invalid JSON format.')
            return questions_data

        if len(questions) != 10:
            errors.append('Each quiz must have exactly 10 questions.')
        for question in questions:
            if len(question['options']) != 4:
                errors.append('Each question must have exactly 4 options.')
            correct_options = [option for option in question['options'] if option['is_correct']]
            if len(correct_options) != 1:
                errors.append('Each question must have exactly one correct option.')

        if errors:
            raise forms.ValidationError(errors)

        return questions_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.questions = json.loads(self.cleaned_data['questions'])
        if commit:
            instance.save()
        return instance
