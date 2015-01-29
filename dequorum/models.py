from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone


class VisibleQuerySet(QuerySet):

    def visible(self):
        return self.filter(is_visible=True)


class Thread(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    # moderators = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    is_open = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)

    tags = models.ManyToManyField('Tag', blank=True)

    objects = VisibleQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('thread-detail', kwargs={'pk': self.pk})


class Message(models.Model):
    thread = models.ForeignKey('Thread', related_name='messages')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    body = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now)
    is_visible = models.BooleanField(default=True)

    objects = VisibleQuerySet.as_manager()


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
