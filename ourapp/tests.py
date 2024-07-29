from django.test import TestCase
from .models import Content, Profile, Quiz
from django.contrib.auth.models import User
import json

class ContentModelTest(TestCase):
    def setUp(self):
        Content.objects.create(title="Test Content", description="Test Description", user="Test User", unit=1)

    def test_content_creation(self):
        content = Content.objects.get(title="Test Content")
        self.assertEqual(content.description, "Test Description")
        self.assertEqual(content.user, "Test User")
        self.assertEqual(content.unit, 1)

class ProfileModelTest(TestCase):
    def setUp(self):
        Profile.objects.create(user="Test User", bio="Test Bio", location="Test Location", birth_date="2000-01-01")

    def test_profile_creation(self):
        profile = Profile.objects.get(user="Test User")
        self.assertEqual(profile.bio, "Test Bio")
        self.assertEqual(profile.location, "Test Location")
        self.assertEqual(profile.birth_date.strftime('%Y-%m-%d'), "2000-01-01")

class QuizModelTest(TestCase):
    def setUp(self):
        questions = [{"question": "Test Question", "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False}, {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]}]
        Quiz.objects.create(unit=1, name="Test Quiz", user="Test User", questions=questions)

    def test_quiz_creation(self):
        quiz = Quiz.objects.get(name="Test Quiz")
        self.assertEqual(quiz.unit, 1)
        self.assertEqual(quiz.user, "Test User")
        self.assertEqual(len(quiz.questions), 1)
        self.assertEqual(quiz.questions[0]['question'], "Test Question")
from django.test import TestCase
from .forms import CreatUserForm, StudentProfileForm, TeacherProfileForm, ContentForm, ProfileForm, QuizForm

class UserRegisterFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'first_name': 'fname', 'last_name': 'lname','username': 'testuser', 'email': 'testuser@gmail.com', 'password1': 'password123@', 'password2': 'password123@'}
        form = CreatUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'username': 'testuser', 'email': 'testuser@example.com', 'password1': 'password123', 'password2': 'password321'}
        form = CreatUserForm(data=form_data)
        self.assertFalse(form.is_valid())

class QuizFormTest(TestCase):
    def test_valid_form(self):
        questions = [{"question": "Test Question", "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False}, {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
                     {"question": "Test Question", "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False}, {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
                     {"question": "Test Question", "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False}, {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
                     {"question": "Test Question", "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False}, {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
                     {"question": "Test Question", "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False}, {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
                     {"question": "Test Question", "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False}, {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
                     {"question": "Test Question", "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False}, {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
                     {"question": "Test Question", "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False}, {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
                     {"question": "Test Question", "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False}, {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
                     {"question": "Test Question", "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False}, {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]}]
        form_data = {'unit': 3, 'name': 'Test Quiz', 'user': 'Test User', 'questions': json.dumps(questions)}
        form = QuizForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        questions = [{"question": "Test Question", "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False}]}]  # Invalid because options are less than 4
        form_data = {'unit': 1, 'name': 'Test Quiz', 'user': 'Test User', 'questions': json.dumps(questions)}
        form = QuizForm(data=form_data)
        self.assertFalse(form.is_valid())
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Content, Profile, Quiz

class RegisterStudentViewTest(TestCase):
    def test_register_student_view(self):
        response = self.client.get(reverse('register_student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_student.html')

class HomePageViewTest(TestCase):
    def test_home_page_view(self):
        response = self.client.get(reverse('HomePage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'HomePage.html')

class AddContentViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_add_content_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('AddContent', kwargs={'username': self.user.username}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'AddContent.html')


from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from .models import Content, Profile, Quiz
from .forms import CreatUserForm, ContentForm, UserRegisterForm, TeacherProfileForm, QuizForm


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.student_group = Group.objects.create(name='Student')
        self.teacher_group = Group.objects.create(name='Teacher')
        self.admin_group = Group.objects.create(name='Admin')
        self.student_user = User.objects.create_user(username='student', password='test123')
        self.teacher_user = User.objects.create_user(username='teacher', password='test123')
        self.admin_user = User.objects.create_superuser(username='admin', password='test123')
        self.student_user.groups.add(self.student_group)
        self.teacher_user.groups.add(self.teacher_group)

        self.content = Content.objects.create(
            title='Sample Content', description='This is a sample content.', user='teacher', unit=3
        )
        self.profile = Profile.objects.create(
            user='student', bio='This is a bio.', location='Location', birth_date='2000-01-01'
        )
        self.quiz = Quiz.objects.create(
            unit=3, name='Sample Quiz', user='teacher', questions='[]'
        )

    def test_register_student(self):
        response = self.client.post(reverse('register_student'), {
            'username': 'newstudent', 'password1': 'testpass123', 'password2': 'testpass123',
            'email': 'student@test.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newstudent').exists())


    def test_home(self):
        response = self.client.get(reverse('HomePage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'HomePage.html')

    def test_teacher_mainpage(self):
        self.client.login(username='teacher', password='test123')
        response = self.client.get(reverse('teacher_mainpage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_mainpage.html')

    def test_login_teacher(self):
        response = self.client.post(reverse('TeacherLogIn'), {
            'username': 'teacher', 'password': 'test123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('teacher_mainpage'))

    def test_admin_login(self):
        response = self.client.post(reverse('AdminLogIn'), {
            'username': 'admin', 'password': 'test123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('HomePageAdmin'))

    def test_homeadmin(self):
        response = self.client.get(reverse('HomePageAdmin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'HomePageAdmin.html')

    def test_teacher_table(self):
        response = self.client.get(reverse('TeacherTable'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'TeacherTable.html')

    def test_student_table(self):
        response = self.client.get(reverse('StudentTable'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'StudentTable.html')

    def test_add_content(self):
        self.client.login(username='teacher', password='test123')
        response = self.client.post(reverse('AddContent', args=['teacher']), {
            'title': 'New Content', 'description': 'This is a new content.', 'unit': 3
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Content.objects.filter(title='New Content').exists())

    def test_content_list(self):
        self.client.login(username='teacher', password='test123')
        response = self.client.get(reverse('ContentList', args=['teacher']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ContentListTeacher.html')

    def test_delete_content(self):
        self.client.login(username='teacher', password='test123')
        response = self.client.post(reverse('delete_content', args=[self.content.pk, 'teacher']))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Content.objects.filter(pk=self.content.pk).exists())

    def test_view_content(self):
        response = self.client.get(reverse('viewContent'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewContent.html')

    def test_add_student(self):
        response = self.client.post(reverse('addstudent'), {
            'username': 'newstudent', 'password1': 'testpass123', 'password2': 'testpass123',
            'email': 'student@test.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newstudent').exists())

    def test_logout(self):
        self.client.login(username='teacher', password='test123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('HomePage'))

    def test_review_teacher_list(self):
        response = self.client.get(reverse('Review_teacher_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Review_teacher_list.html')

    def test_review_student_list(self):
        response = self.client.get(reverse('Review_Student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Review_Student_list.html')

    def test_edit_profile(self):
        self.client.login(username='student', password='test123')
        response = self.client.post(reverse('EditProfileStudent', args=['student']), {
            'bio': 'Updated bio', 'location': 'Updated location', 'birth_date': '2000-01-01'
        })
        self.assertEqual(response.status_code, 302)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.bio, 'Updated bio')

    def test_update_content(self):
        self.client.login(username='teacher', password='test123')
        response = self.client.post(reverse('Update_Content', args=[self.content.pk, 'teacher']), {
            'title': 'Updated Content', 'description': 'This is updated content.', 'unit': 3
        })
        self.assertEqual(response.status_code, 302)
        self.content.refresh_from_db()
        self.assertEqual(self.content.title, 'Updated Content')

    def test_student_login(self):
        response = self.client.post(reverse('StudentLogIn'), {
            'username': 'student', 'password': 'test123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('HomePageStudent'))

    def test_add_teacher(self):
        response = self.client.post(reverse('AddTeacher'), {
            'username': 'newteacher', 'password1': 'testpass123', 'password2': 'testpass123',
            'email': 'teacher@test.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newteacher').exists())

    def test_create_quiz(self):
        self.client.login(username='teacher', password='test123')
        questions = [
            {"text": "Question 1",
             "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False},
                         {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
            {"text": "Question 2",
             "options": [{"text": "Option 1", "is_correct": False}, {"text": "Option 2", "is_correct": True},
                         {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
            {"text": "Question 3",
             "options": [{"text": "Option 1", "is_correct": False}, {"text": "Option 2", "is_correct": False},
                         {"text": "Option 3", "is_correct": True}, {"text": "Option 4", "is_correct": False}]},
            {"text": "Question 4",
             "options": [{"text": "Option 1", "is_correct": False}, {"text": "Option 2", "is_correct": False},
                         {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": True}]},
            {"text": "Question 5",
             "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False},
                         {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
            {"text": "Question 6",
             "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False},
                         {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
            {"text": "Question 7",
             "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False},
                         {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
            {"text": "Question 9",
             "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False},
                         {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
            {"text": "Question 9",
             "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False},
                         {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]},
            {"text": "Question 10",
             "options": [{"text": "Option 1", "is_correct": True}, {"text": "Option 2", "is_correct": False},
                         {"text": "Option 3", "is_correct": False}, {"text": "Option 4", "is_correct": False}]}]