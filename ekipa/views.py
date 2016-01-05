from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from news.models import News


class HomePageView(ListView):
    template_name = 'ekipa/index.html'
    queryset = News.objects.all().order_by('-publication_date')[:5]
