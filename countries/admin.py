from django.contrib.admin import register, ModelAdmin
from .models import Country, CountrySubscription
from common.custom_admin import ReadOnlyAdmin


@register(Country)
class CountryAdmin(ReadOnlyAdmin):
    list_display = ["name", "capital", "region"]
    list_display_links = ["name", "capital", "region"]
    search_fields = ("name", "capital", "region")
    ordering = ("name",)

    def has_change_permission(self, request, obj=None):
        return True


@register(CountrySubscription)
class CountrySubscription(ReadOnlyAdmin):
    list_display = ["user", "country"]
    list_display_links = ["user", "country"]
