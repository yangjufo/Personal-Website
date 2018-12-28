from django.shortcuts import render

def about(request):
    return render(request, 'basic/about.html', context={})

def project(request):
    return render(request, 'project/index.html', context={})

def contact(request):
    return render(request, 'basic/contact.html', context={})