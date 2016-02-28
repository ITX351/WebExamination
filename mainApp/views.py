from django.shortcuts import *
from django.views.generic import ListView

from mainApp.models import Problem
from mixin.common_mixin import BaseMixin


def login(request):
    return render(request, 'mainApp/login.html', {})


def homepage(request):
    return render(request, 'mainApp/index.html', {})


class ProblemListView(BaseMixin, ListView):
    template_name = 'mainApp/problem/index.html'
    context_object_name = 'problem_list'
    model = Problem

    def get_context_data(self, *args, **kwargs):
        context = super(ProblemListView, self).get_context_data(*args, **kwargs)
        return context
