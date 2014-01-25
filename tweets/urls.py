from django.conf.urls import patterns, url

from tweets import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^scrapper/$', views.scrapper, name='scrapper'),
    url(r'^piechart/$', views.piechart, name='piechart'),
    url(r'^linechart/$', views.linechart, name='linechart'),



)