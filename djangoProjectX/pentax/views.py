from django.shortcuts import HttpResponse, render


def hello(request):
    return HttpResponse('<h3>Hello ooooo!</h3>')


def hello_file(request):
    return render(request, 'hello-file.html')


def landing_page(request):
    return render(request, 'landing_page.html')
