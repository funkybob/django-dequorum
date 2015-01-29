from django.conf import settings
from django.db import models
from django.utils import timezone


class Thread(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    # moderators = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    is_open = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)

    tags = models.ManyToManyField('Tag')


class Message(models.Model):
    thread = models.ForeignKey('Thread', related_name='messages')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    body = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now)
    is_visible = models.BooleanField(default=True)


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
