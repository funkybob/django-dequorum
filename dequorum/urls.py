from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.thread_list, name='thread-list'),
    url(r'^add/$', views.thread_create, name='thread-create'),
    url(r'^(?P<pk>\d+)/$', views.thread_detail, name='thread-detail'),
    url(r'^(?P<pk>\d+)/add/$', views.message_create, name='message-create'),
]
