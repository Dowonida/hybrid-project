from django import forms
from .models import Movie, Comment

class Movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description')

class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)