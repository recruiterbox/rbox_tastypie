from builtins import range
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Definition(models.Model):
    word = models.CharField(max_length=255)
    content = models.TextField()

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()


class Quote(models.Model):
    byline = models.CharField(max_length=255)
    content = models.TextField()


class Rating(models.Model):
    RATINGS = [ (x, x) for x in range(1, 6) ]

    rating = models.PositiveIntegerField(choices=RATINGS, default=3)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
