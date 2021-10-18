from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Book, Review


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "book_list"
    login_url = "account_login"
    paginate_by = 20


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    login_url = "account_login"
    permission_required = "books.special_status"

    def post(self, request, *args, **kwargs):
        next_ = request.POST.get('next', '/')
        book_id = next_.split("/")[-1]
        user_review = request.POST.get('review', "")
        if not user_review:
            return redirect(next_)
        # book
        book = get_object_or_404(Book, id=book_id)
        # create review
        Review.objects.create(
            book=book,
            author=request.user,
            review=user_review,
        )
        return redirect(next_)


class SearchListView(ListView):
    model = Book
    context_object_name = "search_list"
    template_name = "books/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
