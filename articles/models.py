from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=300)
    optionA = models.TextField(default='')
    optionB = models.TextField(default='')
    # like = models.IntegerField(default=0)

    # comment_set = 


class Comment(models.Model):
    content = models.TextField(default='')
    choice = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B')])
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id = 