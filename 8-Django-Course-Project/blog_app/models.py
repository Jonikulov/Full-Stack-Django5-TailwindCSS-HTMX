from django.db import models
from django.contrib.auth.models import AbstractUser

ARTICLE_STATUSES = (
    # database value, template/rendering value
    ("draft", "draft"),
    ("inprogress", "in progress"),
    ("published", "published"),
)

class UserProfile(AbstractUser):
    pass


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default="")
    word_count = models.IntegerField()
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20,
        choices=ARTICLE_STATUSES,
        default="draft"
    )
    # auto_now_add - only executes once on INSERT, first creation only
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now - executes on every UPDATE, every save/update
    updated_at = models.DateTimeField(auto_now=True)
