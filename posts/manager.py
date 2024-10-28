from django.db.models import Manager
from .queryset import PostQuerySet


class CustomPostManager(Manager):

    def get_queryset(self):
        return PostQuerySet(model=self.model, using=self._db, hints=self._hints)