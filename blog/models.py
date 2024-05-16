from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GolfCourse(models.Model):
    name = models.CharField(max_length=50)
    location = models.Charfield(max_length=50)
    holes_amount = models.IntegerField()
    extra_facilities = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    golf_course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating =  models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"


