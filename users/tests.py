from users.views import SignupPageView
from django.urls.base import resolve
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CustomUserTests(TestCase):
    def test_create_user(self):
        """Tests create user"""
        User = get_user_model()

        user = User.objects.create_user(
            username="kbg", email="kbg@kb8.com", password="testkbg123"
        )
        self.assertEqual(user.username, "kbg")
        self.assertEqual(user.email, "kbg@kb8.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Test creating superuser"""
        User = get_user_model()

        user = User.objects.create_superuser(
            username="kgb", email="kgb@kb8.com", password="testkgb123"
        )
        self.assertEqual(user.username, "kgb")
        self.assertEqual(user.email, "kgb@kb8.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupPageTests(TestCase):
    """Sign Up page tests."""

    def setUp(self) -> None:
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        """Testing signup template"""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_signup_form(self):
        """Testing signup form"""
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        """Testing signup view"""
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
