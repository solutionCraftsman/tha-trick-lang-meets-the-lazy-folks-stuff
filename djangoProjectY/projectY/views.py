from django.shortcuts import HttpResponse


def hello_world(request):
    return HttpResponse('<h1>Hello Dam Dam Baby</h1>')

