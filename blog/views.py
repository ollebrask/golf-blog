from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Review
from .forms import ReviewForm

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

# To show a certain review upscaled and with content.
def review_detail(request, review_id):
    # https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'blog/review_detail.html', {'review': review})

#To add a review.
@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added successfully!')
            return redirect('show_reviews')
    else:
        form = ReviewForm()
    return render(request, 'blog/add_review.html', {'form': form})

#To edit a review
@login_required
def edit_Review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review updated succesfully!')
            return redirect('review_detail', review_id=review.id)
    else:
        form= ReviewForm(instance=review)
