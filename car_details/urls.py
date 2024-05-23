from django.urls import path
from .views import compare_prices_view

urlpatterns = [
    path('compare-prices/', compare_prices_view, name='compare_prices'),
]
