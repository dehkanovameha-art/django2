from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Article


# 🔹 список всех статей
def archive(request):
    posts = Article.objects.all().order_by('-created_date')
    return render(request, 'archive.html', {"posts": posts})


# 🔹 одна статья
def get_article(request, article_id):
    post = get_object_or_404(Article, id=article_id)
    return render(request, 'article.html', {"post": post})


# 🔹 создание статьи
def create_post(request):
    if not request.user.is_anonymous:

        if request.method == "POST":
            form = {
                'text': request.POST.get("text"),
                'title': request.POST.get("title")
            }

            if form["text"] and form["title"]:

                # проверка уникальности
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = "Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})

                article = Article.objects.create(
                    text=form["text"],
                    title=form["title"],
                    author=request.user
                )

                return redirect('get_article', article_id=article.id)

            else:
                form['errors'] = "Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})

        else:
            return render(request, 'create_post.html', {})

    else:
        raise Http404
