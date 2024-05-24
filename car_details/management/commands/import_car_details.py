import json
import os
from django.core.management.base import BaseCommand
from car_details.models import CarDetail, Category, SubCategory


class Command(BaseCommand):
    help = 'Import car details from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')
        parser.add_argument('category_name', type=str, help='Category name')
        parser.add_argument('subcategory_name', type=str, help='Subcategory name')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        category_name = kwargs['category_name']
        subcategory_name = kwargs['subcategory_name']

        if not os.path.exists(file_path):
            self.stderr.write(f"File '{file_path}' does not exist.")
            return

        category, _ = Category.objects.get_or_create(name=category_name)
        subcategory, _ = SubCategory.objects.get_or_create(name=subcategory_name, category=category)

        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                self.stderr.write(f"Error reading JSON file: {e}")
                return

            for item in data:
                title = item.get('name')
                price = item.get('price')
                url = item.get('url')
                image = item.get('image')

                if not title or not price or not url or not image:
                    self.stderr.write(f"Missing data in item: {item}")
                    continue

                try:
                    price = float(price.replace(' грн', '').replace('грн', '').strip())
                except ValueError:
                    self.stderr.write(f"Invalid price value: {price}")
                    continue

                CarDetail.objects.create(title=title, price=price, url=url, image=image, subcategory=subcategory)
                self.stdout.write(f"Added car detail: {title} with price {price} to subcategory {subcategory.name}")

        self.stdout.write(self.style.SUCCESS('Successfully imported car details'))
