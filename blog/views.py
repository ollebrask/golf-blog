from django.shortcuts import render
from django.views import generic
from .models import Review

# Create your views here.
def index(request):
    latest_reviews = Review.objects.order_by('-created_on')[:3]
    return render(request, 'blog/index.html', {'latest_reviews': latest_reviews})

# To show all reviews as paginated list, 6 per page.
def show_reviews(request):
    reviews_list = Review.object.all()
    paginator = Paginator(reviews_list, 6)
    page_number = request.GET.get('page')
    reviews_page = paginator.get_page(page_number)

    return render(request, 'show_reviews.html', {'reviews.page': reviews_page})