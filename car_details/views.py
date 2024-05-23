from django.shortcuts import render
from .utils import find_lowest_price_among_subcategories, get_sorted_details_among_subcategories


def compare_prices_view(request):
    subcategory_names = ['bampers_motoland', 'bampers_autoliga', 'bampers_other']

    lowest_price_result = find_lowest_price_among_subcategories(subcategory_names)

    sorted_details = get_sorted_details_among_subcategories(subcategory_names)

    context = {
        'lowest_price_result': lowest_price_result,
        'sorted_details': sorted_details,
    }
    return render(request, 'car_details/compare_prices.html', context)


