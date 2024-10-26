from django.contrib.admin import register, ModelAdmin
from .models import Post


@register(Post)
class PostAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

