from django.contrib import admin
from .models import GolfCourse, Review, Comment

# Register your models here.
admin.site.register(GolfCourse)
admin.site.register(Review)
admin.site.register(Comment)