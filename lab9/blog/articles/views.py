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
    from django.contrib.auth.models import User
    

from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
            "email": request.POST.get("email"),
        }

        if not form["username"] or not form["password"]:
            form["errors"] = "Заполните все поля"
            return render(request, "register.html", {"form": form})

        try:
            User.objects.get(username=form["username"])
            form["errors"] = "Пользователь уже существует"
            return render(request, "register.html", {"form": form})
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=form["username"],
                email=form["email"],
                password=form["password"]
            )
            return redirect('archive')

    return render(request, "register.html", {})
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return render(request, "login.html", {"error": "Заполните все поля"})

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('archive')
        else:
            return render(request, "login.html", {"error": "Неверный логин или пароль"})

    return render(request, "login.html")


