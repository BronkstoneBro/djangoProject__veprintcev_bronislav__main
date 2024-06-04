from car_details.models import SubCategory


def find_lowest_price_among_subcategories(subcategory_names):
    lowest_price_detail = None

    for subcategory_name in subcategory_names:
        try:
            subcategory = SubCategory.objects.get(name=subcategory_name)
        except SubCategory.DoesNotExist:
            continue

        details = subcategory.car_details.all().order_by('price')
        if details.exists():
            min_price_detail = details.first()
            if lowest_price_detail is None or min_price_detail.price < lowest_price_detail.price:
                lowest_price_detail = min_price_detail

    if lowest_price_detail is None:
        return "No car details found in the provided subcategories."

    return (f"The lowest price is in SubCategory {lowest_price_detail.subcategory.name}: "
            f"{lowest_price_detail.title} at {lowest_price_detail.price} грн.")


def get_sorted_details_among_subcategories(subcategory_names):
    all_details = []

    for subcategory_name in subcategory_names:
        try:
            subcategory = SubCategory.objects.get(name=subcategory_name)
        except SubCategory.DoesNotExist:
            continue

        details = subcategory.car_details.all()
        all_details.extend(details)

    sorted_details = sorted(all_details, key=lambda x: x.price)
    return [{
        'title': detail.title,
        'price': detail.price,
        'subcategory_name': detail.subcategory.name,
        'url': detail.url,
        'image': detail.image,
    } for detail in sorted_details]
