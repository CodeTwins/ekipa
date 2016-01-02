from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, DetailView

from news.models import News


class NewsListView(ListView):
    template_name = 'news/news_list.html'

    model = News
    queryset = News.objects.all().order_by('-publication_date')[:10]


class NewsDetailView(DetailView):
    template_name = 'news/news_detail.html'

    model = News
    context_object_name = 'news'
