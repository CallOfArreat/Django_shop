import datetime
import json
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.shortcuts import render, get_object_or_404
import random
from basketapp.models import Basket
from .models import ProductCategory, Product


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def main(request):
    title = 'Главная'

    products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:3]

    content = {
        'title': title,
        'products': products,
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None, page=1):
    title = 'Продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                'price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            # 'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    title = 'О нас'
    visit_date = datetime.datetime.now()

    content = {
        'title': title,
        'visit_date': visit_date,
    }
    return render(request, 'mainapp/contact.html', content)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    title = product.name
    content = {
        'title': title,
        'product': product,
        'links_menu': ProductCategory.objects.filter(is_active=True),
        'same_products': get_same_products(product)
    }
    return render(request, 'mainapp/product.html', content)
