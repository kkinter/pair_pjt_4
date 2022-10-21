from django.forms import ModelForm
from django import forms
from .models import Review, Comment



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = (
            'title',
            'content',
            'movie_name',
            'grade',
            'image',
        )

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = (
            'user',
            'review',
        )

# 검색 폼 > <input type="text" name="search_word" label="Search Word"> 과 유사
class ReviewSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')