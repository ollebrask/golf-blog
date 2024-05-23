from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('reviews/', views.show_reviews, name='show_reviews'),
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),
    path('review/add/', views.add_review, name='add_review'),
]