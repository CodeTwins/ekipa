from django.conf.urls import patterns, url

from ekipa.views import HomePageView

urlpatterns = patterns('',
    # ListView
    url(r'^$', HomePageView.as_view(), name='home-page'),
)
