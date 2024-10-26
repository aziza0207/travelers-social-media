from django.db.models import (QuerySet, Count)


class UserQuerySet(QuerySet):
    """Для возможности использования кверисета необходимо вначале вызвать .all()."""

    def annotate_posts_count(self):
        return self.annotate(posts_count=Count("author_posts"))

    def annotate_countries_count(self):
        return self.annotate(countries_count=Count("author_posts__country", distinct=True))
