from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /urls/
    url(r'^index/$', views.index, name='index'),
    # ex: /urls/
    url(r'^shorten/(?P<long_url>[-\w]+)$', views.encode),
    # ex: /urls/5/
    url(r'^(?P<short_url>[0-9a-zA-Z]+)$', views.decode, name='decode'),
]
