# Generated by Django 5.0.7 on 2024-08-02 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_content_article_optiona_article_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='optionA',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='optionB',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='choice',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
