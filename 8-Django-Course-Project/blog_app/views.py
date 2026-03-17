from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog_app.models import Article

def home(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.all()
    return render(request, "blog_app/home.html", {"articles": articles})
