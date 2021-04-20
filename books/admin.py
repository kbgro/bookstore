from django.contrib import admin

from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin View for Book"""

    list_display = (
        "title",
        "author",
        "price",
    )
    list_filter = ("author",)
    search_fields = (
        "title",
        "author",
    )
    ordering = ("author",)
    inlines = [ReviewInline]
