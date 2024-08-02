from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)


def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()

    comments = Comment.objects.filter(article_id=id)

<<<<<<< HEAD

    choices = list(comments.values_list('choice', flat=True))
    count_a = choices.count('A')
    count_b = choices.count('B')
    total = count_a + count_b
    if total == 0:
        share_a = 0
        share_b = 0
    else:
        share_a = round(count_a / total * 100)
        share_b = round(count_b / total * 100)

=======
    #commnts_vs = 
>>>>>>> 4acfa4da03fb075ea6d888b4c9537cc4da821796
    context = {
        'article': article,
        'form': form,
        'comments': comments,
        'share_a': share_a,
        'share_b': share_b,
    }

    return render(request, 'detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # if form.is_valid():
        #     article = form.save()
        #     return redirect('articles:detail', id=article.id)
        article = form.save()
        return redirect('articles:detail', id=article.id)

    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)


def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            comment = form.save(commit=False)

            # 1. 객체를 저장하는 방법
            # article = Article.objects.get(id=article_id)
            # comment.article = article
            # comment.save()

            # 2. integer(숫자)를 저장하는 방법
            comment.article_id = article_id
            comment.save()

            return redirect('articles:detail', id=article_id)

    else:
        return redirect('articles:index')


def comment_delete(request, article_id, id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=id)
        comment.delete()
    
    return redirect('articles:detail', id=article_id)

