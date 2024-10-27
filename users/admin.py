from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import register, ModelAdmin
from .models import User, UserSubscription
from common.custom_admin import ReadOnlyAdmin


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "is_blocked",
        "is_allowed_post"

    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    list_display_links = ("first_name",
                          "last_name",
                          "email",)

    search_fields = ("email", "first_name", "last_name")

    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)


@register(UserSubscription)
class UserSubscription(ReadOnlyAdmin):
    list_display = ["subscriber", "subscribed_to"]
    list_display_links = ["subscriber", "subscribed_to"]
