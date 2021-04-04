from django.test.testcases import SimpleTestCase
from django.urls.base import reverse


class HomepageTests(SimpleTestCase):
    """Home page view tests."""

    def setUp(self) -> None:
        url = reverse("home")
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        """Testing status code."""
        self.assertEqual(self.response.status_code, 200)

    def test_hompage_template(self):
        """Testing Templates"""
        self.assertTemplateUsed(self.response, "home.html")

    def test_hompage_contains_correct_html(self):
        """Testing HTML"""
        self.assertContains(self.response, "Homepage")

    def test_hompage_does_not_contains_incorrect_html(self):
        """Testing HTML not containing incorrect html"""
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
