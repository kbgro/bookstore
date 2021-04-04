from django.test.testcases import SimpleTestCase
from django.urls.base import reverse


class HomepageTests(SimpleTestCase):
    """Home page view tests."""

    def test_home_page_status_code(self):
        """Testing status code."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_name(self):
        """Testing url name"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_hompage_template(self):
        """Testing Templates"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_hompage_contains_correct_html(self):
        """Testing HTML"""
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Homepage")

    def test_hompage_does_not_contains_incorrect_html(self):
        """Testing HTML not containing incorrect html"""
        response = self.client.get(reverse("home"))
        self.assertNotContains(response, "Hi there! I should not be on the page.")
