from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):

        return render(request, 'index.html')

class AboutPageView(TemplateView):
    # A different way of doing it
    template_name = "about.html"