from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from .models import User


def users_list(request):
    if request.GET['age'] != '25':
        raise Http404()
    users = User.objects.all()
    return render(request, 'myapp/index.html', context={'users': users})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
