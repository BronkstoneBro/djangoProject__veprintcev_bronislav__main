from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class CarDetail(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    subcategory = models.ForeignKey(SubCategory, related_name='car_details', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
