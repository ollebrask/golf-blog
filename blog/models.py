from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)


# Create your models here.
class GolfCourse(models.Model):
    """ GolfCourse model """
    name = models.CharField(
        max_length=50,
        unique=True,
        validators=[MinLengthValidator(5)]
    )
    location = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)]
    )
    holes_amount = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    extra_facilities = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Review(models.Model):
    """ Review model """
    title = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(5)]
    )
    slug = models.SlugField(max_length=100, unique=True)
    golf_course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    """ Comment model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.review.title}"

    class Meta:
        ordering = ['created_on']
