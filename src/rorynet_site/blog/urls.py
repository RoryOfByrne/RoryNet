from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BlogHomeView.as_view()),
    url(r'^view/(?P<slug>[^\.]+)$', views.BlogPostView.as_view(), name="view_blog_post"),
    url(r'^category/(?P<slug>[^\.]+)$', views.CategoryView.as_view(), name="view_blog_category"),
]