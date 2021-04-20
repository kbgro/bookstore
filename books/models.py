import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Book(models.Model):

    id = models.UUIDField(_("Id"), primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=200)
    author = models.CharField(_("Author"), max_length=200)
    price = models.DecimalField(_("Price"), max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _("book")
        verbose_name_plural = _("books")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return absolute url for Book."""
        return reverse("book_detail", kwargs={"pk": self.pk})


class Review(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    review = models.CharField(_("User Review"), max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")

    def __str__(self):
        return self.review

    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"pk": self.pk})
