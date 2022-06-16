from django.views.generic import ListView
# from pyexpat import model
# from re import template
# from django.shortcuts import render

# Create your views here.
from .models import Articles

class ArticlesView(ListView):
    model = Articles
    template_name = 'index.html'