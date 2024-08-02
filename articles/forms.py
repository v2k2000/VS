from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bg-primary',
            }
        )
    )

    class Meta():
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment

        widgets = {
            'choice': forms.RadioSelect(choices=[('A', 'A'), ('B', 'B')]),
        }

        exclude = ('article', )

