from django.urls import path
from .views import homeView, portfolioView


urlpatterns = [
    path('', homeView, name="home"),
    path('portfolio', portfolioView, name="portfolio")
]
