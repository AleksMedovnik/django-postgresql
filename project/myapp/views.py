from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404, HttpResponse
from .models import User


def users_list(request):
    users = User.objects.all()
    return render(request, 'myapp/index.html', context={'users': users})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def check_name(request):
    if int(request.GET['age']) < 18:
        raise Http404()
    return HttpResponse(f'<h1>Hello, {request.GET["name"]}!</h1>')








