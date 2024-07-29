from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth.models import User,AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Unique related_name for groups
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='custom_user_group',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Unique related_name for user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user_permission',
    )


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

class Content(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.CharField(max_length=255,null=True)
    unit= models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.CharField(max_length=255,null=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.user


from django.core.exceptions import ValidationError
from django.db import models


class Quiz(models.Model):
    unit= models.IntegerField(default=0)

    name = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    questions = models.JSONField()

    # def clean(self):
    #     errors = []
    #     if not self.questions:
    #         errors.append('Questions field cannot be empty.')
    #     if len(self.questions) != 10:
    #         errors.append('Each quiz must have exactly 10 questions.')
    #     for question in self.questions:
    #         if len(question['options']) != 4:
    #             errors.append('Each question must have exactly 4 options.')
    #         correct_options = [option for option in question['options'] if option['is_correct']]
    #         if len(correct_options) != 1:
    #             errors.append('Each question must have exactly one correct option.')
    #
    #     if errors:
    #         raise ValidationError(errors)

    def __str__(self):
        return self.name
