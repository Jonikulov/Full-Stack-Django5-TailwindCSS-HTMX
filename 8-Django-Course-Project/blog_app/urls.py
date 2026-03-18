from django.urls import path

from blog_app.views import home, create_article, ArticleCreateView

urlpatterns = [
    path("", home, name="home"),
    # path("articles/create/", create_article, name="create_article"),
    path("articles/create/", ArticleCreateView.as_view(), name="create_article"),
]
