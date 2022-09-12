from django import forms
from .models import Art


# class Artform(forms.Form):
#     title2=forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

#     Genre=[(1,'공포'),
#     (2,'로맨스'),
#     (3,'코미디'),
#     ]
#     genre = forms.ChoiceField(choices=Genre)


class Artform(forms.ModelForm):

    class Meta:
        model = Art
        fields = ('title','content')