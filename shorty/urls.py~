from django.conf.urls import patterns, url

from shorties import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^[a-zA-Z0-9+/]+={0,2}$', views.trimed),
)
