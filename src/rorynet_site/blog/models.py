from django.db import models
from django.db.models import permalink
from django.utils import timezone

from tinymce.models import HTMLField

class Blog(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    body = HTMLField()

    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    category = models.ForeignKey('blog.Category')

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, {'slug': self.slug})


