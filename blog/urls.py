from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.client_list, name='client_list'),
    url(r'^client/(?P<pk>[0-9]+)/$', views.client_detail, name='client_detail'),
    url(r'^client/new/$', views.client_new, name='client_new'),
    url(r'^client/(?P<pk>[0-9]+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^client/(?P<pk>[0-9]+)/build/$', views.client_build, name='client_build'),
  #  url(r'^client/(?P<pk>[0-9]+)/build/submit/$', views.client_build_submit, name='client_build_submit'),
]