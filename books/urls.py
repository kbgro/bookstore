from django.urls import path

from books.views import BookDetailView, BookListView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<int:pk>", BookDetailView.as_view(), name="book_detail"),
]
