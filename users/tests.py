from django.contrib.auth import get_user_model
from django.test import TestCase


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
