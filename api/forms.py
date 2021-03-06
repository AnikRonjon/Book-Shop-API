from django import forms
from .models import Category, Post, Comment


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


