from django.conf.urls import patterns, include, url
from django.contrib import admin
from django_test.api import ArticleResource

article_resource = ArticleResource()

urlpatterns = patterns('',
    url(r'^all/$', 'article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^language/(?P<language>[a-z\-]+/$', 'article.views.language'),
    url(r'^create/$', 'article.views.create'),
    url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'),
    url(r'^add_comment/(?P<article_id>\d+)/$', 'article.views.add_comment'),
    url(r'^delete_comment/(?P<comment_id>\d+)/$', 'article.views.delete_comment'),
    url(r'^search/$', 'article.views.search_titles'),
    url(r'^api/', include(article_resource.urls))
)