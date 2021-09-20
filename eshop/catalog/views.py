from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Category, Product


def home(request):
    cat = Category.objects.all()
    return render(
        request,
        'catalog/home.html',
        {"categories": cat}
    )


def category_view(request, category_slug):
    cat = Category.objects.get(slug=category_slug)
    return HttpResponse(cat.name)


def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    return HttpResponse(product.name)


def product_list_view(request):
    product = Product.objects.all()
    return render(
        request,
        'catalog/product.html',
        {"products": product}
    )

