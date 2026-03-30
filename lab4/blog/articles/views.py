from django.shortcuts import render, get_object_or_404
from .models import Article

# Страница со списком всех постов
def archive(request):
    posts = Article.objects.all().order_by('-created_date')
    return render(request, 'archive.html', {"posts": posts})

# Страница отдельной статьи
def get_article(request, article_id):
    post = get_object_or_404(Article, id=article_id)
    return render(request, 'article.html', {"post": post})
# Create your views here.
