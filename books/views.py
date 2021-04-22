from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.views.generic import DetailView, ListView

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "book_list"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    login_url = "account_login"
    permission_required = "books.special_status"


class SearchListView(ListView):
    model = Book
    context_object_name = "search_list"
    template_name = "books/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
