from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class AccountTest(TestCase):
    def test_login_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Log In')
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Log In')
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign Up')
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign Up')
        self.assertTemplateUsed(response, 'registration/signup.html')
