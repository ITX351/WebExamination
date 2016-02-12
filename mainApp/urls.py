from django.conf.urls import url

from mainApp import views

urlpatterns = [
    url(r'^$', views.test, name = 'index'),
]
