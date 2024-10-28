from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.db.models import Count, Prefetch
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from posts.models import Post
from ..models import Country
from ..serializers import CountryListSerializer, CountryDetailSerializer
from common.permissions import IsAuthenticatedNotAdmin


@extend_schema(tags=["Country"])
class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticatedNotAdmin,)
    lookup_field = "slug"

    def get_queryset(self):
        queryset = Country.objects.annotate(post_count=Count("country_posts")).filter(
            post_count__gt=0
        )
        if self.action == self.list.__name__:
            return queryset
        return queryset.prefetch_related(
            Prefetch(
                "country_posts", queryset=Post.objects.all().select_related("author").order_by("created_at")
            ))

    def get_serializer_class(self):
        if self.action == self.list.__name__:
            return CountryListSerializer
        else:
            return CountryDetailSerializer

    @method_decorator(cache_page(60 * 20))
    def list(self, request, *args, **kwargs):
        return super(CountryViewSet, self).list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 20))
    def retrieve(self, request, *args, **kwargs):
        return super(CountryViewSet, self).retrieve(request, *args, **kwargs)
