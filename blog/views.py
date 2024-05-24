from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Review, GolfCourse, Comment
from .forms import CommentForm
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
    comments = review.comment_set.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('account_login')
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            messages.success(request, 'Your comment has been posted!')
            return redirect('review_detail', review_id=review.id)
    else:
        comment_form = CommentForm()
   
    return render(request, 'blog/review_detail.html', {
            'review': review,
            "comments": comments,
            "comment_form": comment_form,
    })

#To add a review.
@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.slug = slugify(review.title)
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added successfully!')
            return redirect('show_reviews')
    else:
        form = ReviewForm()
    return render(request, 'blog/add_review.html', {'form': form})

#To edit a review
@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.slug = slugify(review.title)
            review.save()
            messages.success(request, 'Your review updated succesfully!')
            return redirect('review_detail', review_id=review.id)
    else:
        form= ReviewForm(instance=review)
    return render(request, 'blog/edit_review.html', {'form': form})

#To delete a review
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted!')
        return redirect('show_reviews')
    return render(request, 'blog/delete_review.html', {'review': review})

#To show all golfcourses
def show_golfcourses(request):
    golfcourses_list = GolfCourse.objects.all()
    paginator = Paginator(golfcourses_list, 8) 
    page_number = request.GET.get('page')
    golfcourses_page = paginator.get_page(page_number)
    
    return render(request, 'blog/show_golfcourses.html', {'golfcourses_page': golfcourses_page})