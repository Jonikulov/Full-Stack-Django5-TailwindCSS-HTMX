from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)

from blog_app.models import Article
from blog_app.forms import CreateArticleForm

def home(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.all()
    return render(request, "blog_app/home.html", {"articles": articles})


# function based view
def create_article(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CreateArticleForm(data=request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            new_article = Article(
                title = form_data["title"],
                status = form_data["status"],
                content = form_data["content"],
                word_count = form_data["word_count"],
                twitter_post = form_data["twitter_post"],
            )
            new_article.save()
            return redirect("home")
    else:
        form = CreateArticleForm()
    return render(request, "blog_app/article_create.html", {"form": form})


class ArticlesListView(ListView):
    template_name = "blog_app/home.html"
    model = Article
    context_object_name = "articles"


# class based view
class ArticleCreateView(CreateView):
    template_name = "blog_app/article_create.html"
    model = Article
    fields = ["title", "status", "content", "word_count", "twitter_post"]
    success_url = reverse_lazy("home")


class ArticleUpdateView(UpdateView):
    template_name = "blog_app/article_update.html"
    model = Article
    fields = ["title", "status", "content", "word_count", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "article"


class ArticleDeleteView(DeleteView):
    template_name = "blog_app/article_delete.html"
    model = Article
    fields = ["title", "status", "content", "word_count", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "article"
