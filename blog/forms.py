from django import forms
from .models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['star', 'comment']
        widgets = {
            'star': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
