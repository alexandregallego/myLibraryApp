from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# Text field is much larger than the Char Field one.


class Book(models.Model):
    # If a category is deleted all of the books belonging to that category will be deleted.
    category = models.ForeignKey(
        Category, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='book_images', blank=True, null=True)
    # to add this field automatically and Django will handle it for us.
    created_at = models.DateTimeField(auto_now_add=True)
    # If a user is deleted also all of the books pertaining to that user will be deleted.
    created_by = models.ForeignKey(
        User, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
