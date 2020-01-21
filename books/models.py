from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(
        _('title'),
        max_length=200,
    )

    released = models.DateField(
        _('release date'),
    )

    pageCount = models.SmallIntegerField(
        _('page count'),
        blank=True,
    )

    language = models.CharField(
        _('language'),
        max_length=100,
        blank=True,
    )

    imageLink = models.URLField(
        _('image link'),
        max_length=300,
        blank=True,
    )

    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    identifiers = models.ForeignKey(industryIdentifiers, on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(
        _('author'),
        max_length=300,
    )


class industryIdentifiers(models.Model):
    type = models.CharField(
        _('type'),
        max_length=200,
    )

    identifier = models.CharField(
        _('identifier'),
        max_length=200,
    )
