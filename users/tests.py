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

    username = "newuser"
    email = "newuser@email.com"

    def setUp(self) -> None:
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        """Testing signup template"""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_signup_form(self):
        """Testing signup form"""
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        self.assertEqual(new_user.email, self.email)
