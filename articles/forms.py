from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    

    class Meta():
        model = Article
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'optionA': forms.TextInput(attrs={'class': 'form-control'}),
            'optionB': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment

        widgets = {
            'choice': forms.RadioSelect(choices=[('A', 'A'), ('B', 'B')]),
        }

        exclude = ('article', )

