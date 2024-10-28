from django.db.models import (QuerySet, Count, Avg)


class PostQuerySet(QuerySet):
    """Для возможности использования кверисета необходимо вначале вызвать .all()."""

    def annotate_rating_count(self):
        return self.annotate(rating_count=Count("ratings__rating"))

    def annotate_rating_avg(self):
        return self.annotate(rating_avg=Avg("ratings__rating"))
