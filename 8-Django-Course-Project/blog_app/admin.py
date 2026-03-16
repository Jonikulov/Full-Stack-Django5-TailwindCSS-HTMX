from django.contrib import admin

from blog_app.models import Article, UserProfile

admin.site.register((Article, UserProfile))
