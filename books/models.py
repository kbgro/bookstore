import uuid

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
