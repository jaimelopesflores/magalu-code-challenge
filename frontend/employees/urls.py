from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<id>\w+)/detail/$', views.detail, name='detail'),
    url(r'^(?P<id>\w+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<id>\w+)/update/$', views.update, name='update'),
    url(r'^(?P<id>\w+)/delete/$', views.delete, name='delete'),
]
