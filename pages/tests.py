from django.test import TestCase
from django.urls import reverse


class PageTest(TestCase):
    def test_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Home Page')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_by_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Home Page')
        self.assertTemplateUsed(response, 'home.html')

    def test_aboutus_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About Us')
        self.assertTemplateUsed(response, 'pages/aboutus.html')

    def test_aboutus_url_by_name(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About Us')
        self.assertTemplateUsed(response, 'pages/aboutus.html')
