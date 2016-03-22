from django.conf.urls import url

from ekipa.views import HomePageView

urlpatterns = [
    # ListView
    url(r'^$', HomePageView.as_view(), name='home-page'),
]
