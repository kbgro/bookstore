from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    """Admin View for CustomUser"""

    list_display = (
        "email",
        "username",
    )
    list_filter = (
        "email",
        "username",
    )
    search_fields = ("username",)
    ordering = ("username",)
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)