from django.shortcuts import render
from django.viws.generic.base import TemplateView

# Create your views here.
class HomePage(TemplateView):

    """
    Docs
    Template Name:
    
    """
    template_name = 'marketing/home.html'