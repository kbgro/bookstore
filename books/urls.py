from django.urls import path

from books.views import BookDetailView, BookListView, SearchListView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>", BookDetailView.as_view(), name="book_detail"),
    path("search/", SearchListView.as_view(), name="search_results"),
]
