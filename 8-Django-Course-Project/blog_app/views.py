from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
                # word_count = form_data["word_count"],
                twitter_post = form_data["twitter_post"],
            )
            new_article.save()
            return redirect("home")
    else:
        form = CreateArticleForm()
    return render(request, "blog_app/article_create.html", {"form": form})


# -----------------------------------------------------------------------------
# function based view
@login_required  # This replaces the 'LoginRequiredMixin'
def create_article(request: HttpRequest) -> HttpResponse:
    # 1. Initialize the form (handles both GET and POST)
    form = CreateArticleForm(data=request.POST or None)

    # 2. Logic for saving
    if request.method == "POST" and form.is_valid():
        # Using .save() is cleaner than manual dictionary access, but it works
        # only for ModelForm -- `CreateArticleForm(forms.ModelForm)`
        article = form.save(commit=False)
        article.creator = request.user 
        article.save()
        return redirect("home")

    # 3. Render the page
    return render(request, "blog_app/article_create.html", {"form": form})
# -----------------------------------------------------------------------------


class ArticlesListView(LoginRequiredMixin, ListView):
    template_name = "blog_app/home.html"
    model = Article
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(
            creator=self.request.user
        ).order_by("-created_at")


# class based view
class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "blog_app/article_create.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "blog_app/article_update.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "article"

    def test_func(self):
        return self.request.user == self.get_object().creator


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "blog_app/article_delete.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "article"

    def test_func(self):
        return self.request.user == self.get_object().creator
