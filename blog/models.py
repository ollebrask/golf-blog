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

