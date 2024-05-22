from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Review

# Create your views here.
def index(request):
    latest_reviews = Review.objects.order_by('-created_on')[:3]
    return render(request, 'blog/index.html', {'latest_reviews': latest_reviews})

# To show all reviews as paginated list, 6 per page.
def show_reviews(request):
    reviews_list = Review.objects.all()
    paginator = Paginator(reviews_list, 6)
    page_number = request.GET.get('page')
    reviews_page = paginator.get_page(page_number)

    return render(request, 'blog/show_reviews.html', {'reviews_page': reviews_page})

# To show a certain review upscaled and with content.abs
def review_detail(request, review_id):
    # https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'review_detail.html', {'review': review})