from django.contrib import admin
from .models import CarDetail


@admin.register(CarDetail)
class CarDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
