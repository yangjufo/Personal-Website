from django.shortcuts import render


def index(request):
    return render(request, 'myprojects/index.html', context={})


def about(request):
    return render(request, 'basic/about.html', context={})
