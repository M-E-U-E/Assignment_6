from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import PropertyOwner


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('user_signup')  # Replace with the actual name of the signup URL
        self.login_url = reverse('user_login')  # Replace with the actual name of the login URL
        self.activation_url = reverse('activation')  # Replace with the actual name of the activation URL
        self.owner_signup_url = reverse('owner_signup')  # Replace with the actual name of the owner signup URL
        self.home_url = reverse('home')  # Replace with the actual name of the home URL

    def test_user_signup_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_user_signup_post_success(self):
        response = self.client.post(self.signup_url, {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 200)  # Activation page is rendered
        self.assertTemplateUsed(response, 'activation.html')
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_signup_post_missing_fields(self):
        response = self.client.post(self.signup_url, {
            'username': '',
            'email': '',
            'password': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'All fields are required!')

    def test_user_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_login_post_success(self):
        user = User.objects.create_user(username='testuser', password='password123')
        user.is_active = True
        user.save()

        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to 'home'
        self.assertRedirects(response, self.home_url)

    def test_user_login_post_inactive_user(self):
        user = User.objects.create_user(username='testuser', password='password123')
        user.is_active = False
        user.save()

        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to 'activation'
        self.assertRedirects(response, self.activation_url)

    def test_user_login_post_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'wronguser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Invalid username or password.')

    def test_activation_page(self):
        response = self.client.get(self.activation_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'activation.html')

    def test_owner_signup_get(self):
        response = self.client.get(self.owner_signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'owner_signup.html')

    def test_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to the Inventory Management System!')
