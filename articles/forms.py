from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):

    class Meta():
        model = Article
        # fields = '__all__'
        exclude = ('like', )


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment

        widgets = {
            'choice': forms.RadioSelect(choices=[('A', 'A'), ('B', 'B')]),
        }

        exclude = ('article', )

