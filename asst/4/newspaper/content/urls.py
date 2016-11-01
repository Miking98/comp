from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.all_articles, name='all_articles'),
    # ex: /1
    url(r'^(?P<article_id>[0-9]+)/$', views.get_article, name='get_article'),
]