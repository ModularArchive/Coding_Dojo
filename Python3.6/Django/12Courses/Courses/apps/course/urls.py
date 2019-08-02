from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^course$', views.course),
    url(r'^course/create$', views.create),
    url(r'^course/(?P<number>\d)/conf_destroy', views.conf_destroy),
    url(r'^course/(?P<number>\d)/destroy', views.destroy),
]