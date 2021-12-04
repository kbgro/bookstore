import json

import stripe
from django.conf import settings
from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from books.models import Book


class OrdersPageView(TemplateView):
    template_name = "orders/purchase.html"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["stripe_key"] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

    def post(self, request, *args, **kwargs):
        post_dict = request.POST.dict()
        items = json.loads(post_dict.get("items"))
        total = float(post_dict.get("total"))
        books = Book.objects.filter(id__in=items)
        print((items, total))
        print(books)
        return redirect("orders")


def charge(request):
    permission = Permission.objects.get(codename="special_status")
    current_user = request.user
    current_user.user_permissions.add(permission)

    if request.method == "POST":
        charge = stripe.Charge.create(
            amount=3900,
            currency="usd",
            description="Purchase all books",
            source=request.POST["stripeToken"],
            api_key=settings.STRIPE_TEST_SECRET_KEY,
        )
    return render(request, "orders/charge.html")
