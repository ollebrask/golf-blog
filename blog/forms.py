from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select())
    
    class Meta:
        model = Review
        fields = ['title', 'golf_course', 'content', 'rating']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4})
        }
        labels = {
            'content': '',
        }