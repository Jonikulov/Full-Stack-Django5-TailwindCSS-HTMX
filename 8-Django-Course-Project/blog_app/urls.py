from django.urls import path

from blog_app.views import home

urlpatterns = [
    path("", home),
]
