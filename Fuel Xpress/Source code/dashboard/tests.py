from django.test import TestCase #we need to import TestCase class from Django test Framework.
from django.urls import reverse #we need to import the reverse function from the Django URL's Module.

class DashboardViewsTests(TestCase):#we create a class named as DashboardViewsTests which is inherits from the TestCase.
    def test_index_view(self): #define a method to test the client to send a GET request.
        response = self.client.get(reverse('index_page'))
        self.assertEqual(response.status_view_code, 200)
        self.assertTemplateUsed(response, 'dashboard/index.html')

    def test_home_view(self):# test client to send a GET request and http response code.
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_view_code, 200)
        self.assertTemplateUsed(response, 'dashboard/home.html')

    def test_about_view(self):#Test client to send GET request and HTTP response.
        response = self.client.get(reverse('about_page'))
        self.assertEqual(response.status_view_code, 200)
        self.assertTemplateUsed(response, 'dashboard/about.html')
