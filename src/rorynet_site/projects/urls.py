from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProjectOverviewView.as_view()),
    url(r'^(?P<project_name>\w+)/$', views.ProjectDetailView.as_view()),
]