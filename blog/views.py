from django.shortcuts import render
from django.views import generic
from .models import Review

# Create your views here.
def index(request):
    latest_reviews = Review.objects.order_by('-created_on')[3]
    return render(request, 'blog/index.html', {'latest_reviews': latest_reviews})