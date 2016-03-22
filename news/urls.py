from django.conf.urls import url

from news.views import NewsListView, NewsDetailView

urlpatterns = [
    # ListView
    url(r'^$', NewsListView.as_view(), name='news-list'),

    # DetailView
    url(r'^(?P<slug>[\w-]*\w)$', NewsDetailView.as_view(), name='news-detail')
]
