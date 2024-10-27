from django.contrib.admin import register, ModelAdmin
from .models import Tag, TagSubscription
from common.custom_admin import ReadOnlyAdmin


@register(Tag)
class TagAdmin(ReadOnlyAdmin):
    list_display = ["name", "created_at"]
    search_fields = ("name", )
    ordering = ("name",)


@register(TagSubscription)
class TagSubscription(ReadOnlyAdmin):
    list_display = ["user", "tag"]
