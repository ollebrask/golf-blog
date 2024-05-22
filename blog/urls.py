from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('reviews/', views.show_reviews, name='show_reviews')
]