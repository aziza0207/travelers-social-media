from django.contrib.admin import register, ModelAdmin, StackedInline
from .models import Post, PostImage, Comment, PostRating
from common.custom_admin import ReadOnlyAdmin


class PostImageInline(StackedInline):
    model = PostImage
    extra = 0


@register(Post)
class PostAdmin(ReadOnlyAdmin):
    inlines = (PostImageInline,)

    def has_change_permission(self, request, obj=None):
        return True

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [field.name for field in self.model._meta.fields if field.name != "is_visible"]
        return []


@register(Comment)
class CommentAdmin(ReadOnlyAdmin):
    list_display = ["content", "user", "post"]


@register(PostRating)
class PostRatingAdmin(ReadOnlyAdmin):
    list_display = ["user", "post", "rating"]
