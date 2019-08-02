from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^randword/clear$', views.clear),
    url(r'^counting/$', views.counting),
]