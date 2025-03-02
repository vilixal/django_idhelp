from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string


def index(request):
    # t_index=render_to_string('idbanklist/index.html')
    # return HttpResponse(t_index)
    data_set = {'title': 'Список банков',
                'description': 'МЕНЮ'}
    return render(request, 'idbanklist/index.html', context=data_set)


def page_not_found(request, exception):
    return redirect('home', permanent=True)
