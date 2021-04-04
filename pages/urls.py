from django.urls import path

from pages.views import HomepageView

urlpatterns = [path("", HomepageView.as_view(), name="home")]
