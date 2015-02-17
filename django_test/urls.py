from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from django_test.api import ArticleResource

from django_test.forms import ContactForm1, ContactForm2, ContactForm3
from django_test.views import ContactWizard

import settings 

article_resource = ArticleResource()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^articles/', include('article.urls')),
                       url(r'^accounts/', include('userprofile.urls')),
                       url(r'^accounts/login/$', 'django_test.views.login'),
                       url(r'^accounts/auth/$', 'django_test.views.auth_view'),
                       url(r'^accounts/loggedin/$', 'django_test.views.loggedin'),
                       url(r'^accounts/invalid/$', 'django_test.views.invalid_login'),
                       url(r'^accounts/logout/$', 'django_test.views.logout'),
                       url(r'^accounts/register/$', 'django_test.views.register_user'),
                       url(r'^accounts/register_success/$', 'django_test.views.register_success'),
                       url(r'^articles/all/$', 'article.views.articles'),
                       url(r'^articles/create/$', 'article.views.create'),
                       url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
                       url(r'^articles/like/(?P<article_id>\d+)/$', 'article.views.like_article'),
                       url(r'^articles/add_comment/(?P<article_id>\d+)/$', 'article.views.add_comment'),
                       url(r'^articles/search/', 'article.views.search_titles'),
                       #url(r'^articles/api/', include(article_resource.urls)),
                       url(r'^contact/', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
)

if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    
    urlpatterns += staticfiles_urlpatterns()