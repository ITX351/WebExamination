from django.conf.urls import url

from mainApp import views

urlpatterns = [
    url(r'^(?:login/)?$', views.login, name = 'login'),
    url(r'^homepage/$', views.homepage, name = 'homepage'),
    url(r'^problems/$', views.ProblemListView.as_view(), name = 'problem_list')
]
