from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Project

class ProjectOverviewView(TemplateView):
    def get(self, request, **kwargs):
        projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'projectsoverview.html', {'projects' : projects})

class ProjectDetailView(TemplateView):
    def get(self, request, **kwargs):
        project = Project.objects.get(id_string=kwargs['project_name'])
        return render(request, 'project.html', {'project' : project})
