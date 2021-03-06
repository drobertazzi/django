from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.conf import settings

urlpatterns = patterns('',
                       url(r'^articles/all/$', 'article.views.articles'),
                       url(r'^get/(?P<article_id>\d+)/$', 
                           'article.views.article'),
                       url(r'^language/(?P<language>[a-z\-]+)/$', 
                           'article.views.language'),
                       url(r'^articles/all/$')
)
#for django_test/django_test
