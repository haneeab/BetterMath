from django.test import TestCase,Client

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ourapp.views import register_student, home, teacher_mainpage, login_teacher, AdminLogIn, homeadmin, TeacherTable, studenttable, AddContent, ContentList, delete_Contant, homestudent, viewContent
from django.contrib.auth.models import User, Group
from ourapp.models import Content
from ourapp.forms import CreatUserForm, ContentForm
from ourapp.urls import path

class TestUrls(SimpleTestCase):

    def test_register_student_url_resolves(self):
        url = reverse('register_student')
        self.assertEqual(resolve(url).func, register_student)

    def test_home_url_resolves(self):
        url = reverse('HomePage')
        self.assertEqual(resolve(url).func, home)

    def test_teacher_mainpage_url_resolves(self):
        url = reverse('teacher_mainpage')
        self.assertEqual(resolve(url).func, teacher_mainpage)

    def test_login_teacher_url_resolves(self):
        url = reverse('TeacherLogIn')
        self.assertEqual(resolve(url).func, login_teacher)

    def test_admin_login_url_resolves(self):
        url = reverse('AdminLogIn')
        self.assertEqual(resolve(url).func, AdminLogIn)

    # Add other URL tests similarly
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from ourapp.models import Content
from ourapp.forms import CreatUserForm, UserRegisterForm, TeacherProfileForm, ContentForm

class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.client = Client()
        self.register_student_url = reverse('register_student')
        self.home_url = reverse('HomePage')
        self.teacher_mainpage_url = reverse('teacher_mainpage')
        self.login_teacher_url = reverse('TeacherLogIn')
        self.admin_login_url = reverse('AdminLogIn')
        self.homeadmin_url = reverse('HomePageAdmin')
        self.teachertable_url = reverse('TeacherTable')
        self.studenttable_url = reverse('StudentTable')
        self.view_content_url = reverse('viewContent')
        self.homestudent_url = reverse('HomePageStudent')

        self.teacher_group = Group.objects.create(name='Teacher')
        self.student_group = Group.objects.create(name='Student')

    def test_register_student_GET(self):
        response = self.client.get(self.register_student_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_student.html')

    def test_register_student_POST(self):
        response = self.client.post(self.register_student_url, {
            'username': 'teststudent',
            'first_name': 'first_name1',
            'last_name': 'last_name1',

            'password1': 'password123',
            'password2': 'password123',
            'email': 'student@test.com'
        })
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, self.home_url)
        # self.assertTrue(User.objects.filter(username='teststudent').exists()
    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'HomePage.html')

    def test_homeadmin_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'HomePage.html')

    # def test_teacher_mainpage_GET(self):
    #
    #     response = self.client.get(self.teacher_mainpage_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'teacher_mainpage.html' ,'teststudent')

    # def test_login_teacher_POST(self):
    #     self.teacher_group.user_set.add(self.user)
    #     response = self.client.post(self.admin_login_url, {
    #         'username': 'testuser',
    #         'password': 'password123'
    #     })
    #     self.assertRedirects(response, self.home_url)

    # def test_admin_login_POST(self):
    #     response = self.client.post(self.admin_login_url, {
    #         'username': 'testuser',
    #         'password': 'password123'
    #     })
    #     self.assertRedirects(response, self.home_url)


    # def test_teachertable_GET(self):
    #     response = self.client.get(self.teachertable_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'TeacherTable.html')
    #
    def test_studenttable_GET(self):
        response = self.client.get(self.studenttable_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'StudentTable.html')

    def test_add_content_POST(self):
        response = self.client.post(reverse('AddContent', args=['testuser']), {
            'title': 'Test Content',
            'description': 'This is a test description',
            'unit': 1
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.home_url)
        self.assertTrue(Content.objects.filter(title='Test Content').exists())

    def test_view_content_GET(self):
        response = self.client.get(self.view_content_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewContent.html')

    def test_homestudent_GET(self):
        response = self.client.get(self.homestudent_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'HomePageStudent.html')
 # def test_content_list_GET(self):
    #     Content.objects.create(title='Test Content', description='Test Description', user='testuser')
    #     response = self.client.get(reverse('ContentList', args=['testuser']))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'ContentListTeacher.html', args=['testuser'])

    # def test_delete_content_POST(self):
    #     content = Content.objects.create(title='Test Content', description='Test Description', user='testuser')
    #     response = self.client.post(reverse('delete_content', args=[content.id, 'testuser']))
    #     self.assertRedirects(response, reverse('ContentList', args=['testuser']))
    #     self.assertFalse(Content.objects.filter(title='Test Content').exists())

from django.test import TestCase
from django.urls import reverse
from ourapp.models import Content  # Adjust this import as per your app structure


class TestContentListView(TestCase):
    def setUp(self):
        # Create a test user and content for testing
        self.testuser = User.objects.create_user(username='testuser', password='password123')
        Content.objects.create(title='Test Content', description='Test Description', user=self.testuser)
    def test_content_list_GET(self):
        # Perform a GET request to the ContentList view for 'testuser'
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('ContentList', args=['testuser']))
        # Check if the response is successful and returns status code 200
        self.assertEqual(response.status_code, 200)
        # Check if the correct template 'ContentListTeacher.html' is used
        self.assertTemplateUsed(response, 'ContentListTeacher.html')
        # Check if the 'contents' context contains the created content
        self.assertIn('contents', response.context)
        self.assertEqual(len(response.context['contents']), 1)  # Adjust as per your test data
        # Check if the rendered content matches the created content's title
        self.assertContains(response, 'Test Content')
