from django.shortcuts import render


def index(request):
    return render(request, 'basic/index.html', context={})


def about(request):
    return render(request, 'basic/about.html', context={})
