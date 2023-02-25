from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class PartColor(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Furniture(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.CharField(max_length=100)
    description_full = models.TextField()
    size = models.CharField(max_length=100)
    price = models.IntegerField()

    colors = models.ManyToManyField(PartColor)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", verbose_name="category", null=True)

    def __str__(self):
        return self.title
