from django.urls import path
from . import views

urlpatterns = [
    path('compare-prices/', views.compare_prices_view, name='compare_prices'),
]
