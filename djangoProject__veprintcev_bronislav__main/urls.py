"""
URL configuration for djangoProject__veprintcev_bronislav__main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from djangoProject__veprintcev_bronislav__main.views import home

# def home(request):
#     return HttpResponse("Hello, Django Unchained! Welcome to the main project.")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('car-details/', include('car_details.urls')),
    path('', home, name='home'),
]
