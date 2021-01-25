from django.shortcuts import render

def homeView(request):
    return render(request, 'home/index.html', {})


def portfolioView(request):
    return render(request, "home/portfolio.html", {})