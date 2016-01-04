from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^client/(?P<cl>[0-9]+)/$', views.client_detail, name='client_detail'),
    url(r'^client/new/$', views.client_new, name='client_new')
]