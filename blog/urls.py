from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('reviews/', views.show_reviews, name='show_reviews'),
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),
    path('review/add/', views.add_review, name='add_review'),
    path('review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
]