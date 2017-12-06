from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Blog, Category

class BlogHomeView(TemplateView):
    def get(self, request, **kwargs):
        blog_posts = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        categories = Category.objects.all()
        return render(request, 'blog_home.html', {'blog_posts' : blog_posts, 'categories' : categories})

class BlogPostView(TemplateView):
    def get(self, request, **kwargs):
        blog_post = get_object_or_404(Blog, slug=kwargs['slug'])
        return render(request, 'blog_post.html', {'blog_post' : blog_post})

class CategoryView(TemplateView):
    def get(self, request, **kwargs):
        category = get_object_or_404(Category, slug=kwargs['slug'])
        return render(request, 'categories.html',
                      {'category' : category, 'blog_posts' : Blog.objects.filter(category=category)})
