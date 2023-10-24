from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Fuelxpress_Profile
from .forms import Fuelxpress_UserRegisterForm

class UsersAppTests(TestCase):
    def test_registration_view(self):
        FE_response = self.client.get(reverse('register'))
        self.assertEqual(FE_response.status_code, 200)

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpwd')
        FE_response = self.client.get(reverse('profile'))
        self.assertEqual(FE_response.status_code, 302)
        self.assertRedirects(FE_response, reverse('login') + '?next=' + reverse('profile'))

    def test_user_register_form_valid(self):
        form_data = {
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password1': 'testpwd',
            'password2': 'testpwd',
        }
        form = Fuelxpress_UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_profile_model(self):
        user = User.objects.create_user(
            username='testuser3',
            email='testuser3@example.com',
            password='testpassword'
        )
        profile = Fuelxpress_Profile.objects.get(user=user)
        self.assertEqual(str(profile), 'testuser3 Profile')
