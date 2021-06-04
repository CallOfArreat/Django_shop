import os

from django.conf import settings

from django.core.management import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser
import json

FILE_PATH = os.path.join(settings.BASE_DIR, 'mainapp/json')


def load_from_json(file_name):
    with open(os.path.join(FILE_PATH, file_name + '.json'), 'r',
              encoding='utf-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)
            # new_category = ProductCategory(**category)
            # такой метод подходит для того, чтобы тут можно еще было какой-то
            # атрибут переопределить или типа того
            # new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            Product.objects.create(**product)
            # new_product = Product(**product)
            # new_product.save()

        # Создаем суперпользователся при промощи менеджера модели
        ShopUser.objects.create_superuser(username='django',
                                          email='some@some.com',
                                          password='geekbrains', age=32)
