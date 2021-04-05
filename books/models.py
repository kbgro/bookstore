from django.db import models
from django.utils.translation import ugettext_lazy as _


class Book(models.Model):

    title = models.CharField(_("Title"), max_length=200)
    author = models.CharField(_("Author"), max_length=200)
    price = models.DecimalField(_("Price"), max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _("book")
        verbose_name_plural = _("books")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("book_detail", kwargs={"pk": self.pk})
