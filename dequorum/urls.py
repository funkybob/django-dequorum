from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.thread_list, name='thread-list'),
]
