from django.db import models
from django.contrib.auth.models import AbstractUser


class Material(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Style(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Palette(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Handle(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Photo(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class User(AbstractUser):
    name = models.CharField(max_length=30, blank=True)
    surname = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=255, blank=True)


# Prefer to create foreign keys to the User model importing the
# settings from django.conf import settings and referring to the settings.AUTH_USER_MODEL
# instead of referring directly to the custom User model.
