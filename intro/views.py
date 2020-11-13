from django.shortcuts import render


def home(request, *args, **kwargs):
    context= {}
    return render(request, '../templates/intro/home.html', context=context)

    
