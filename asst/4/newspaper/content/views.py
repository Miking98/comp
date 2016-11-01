from django.shortcuts import render
from .models import Article

import pprint

def all_articles(request):
    articles = Article.objects.all()
    data = { 'articles': articles }
    return render(request, 'content/all_articles.html', data)

def get_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    data = { 'article': article }
    return render(request, 'content/get_article.html', data)