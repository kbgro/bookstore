from django.test.testcases import SimpleTestCase
from django.urls.base import resolve, reverse

from .views import AboutPageView, HomePageView


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

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        """status code"""
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        """template used"""
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):
        """check contains correct html"""
        self.assertContains(self.response, "About")

    def test_aboutpage_does_not_contain_incorrect_html(self):
        """check contains incorrect html"""
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_aboutpage_url_resolves_aboutpageview(self):
        """check url resove to AboutPageView"""
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
