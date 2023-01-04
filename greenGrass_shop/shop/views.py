from django.shortcuts import render, get_list_or_404
from .models import Category, Product


def main_page(request):
    return render(request,
                  'shop/index.html',
                  )


def product_detail(request, id, slug):
    product = get_list_or_404(
        Product,
        id=id,
        slug=slug,
        available=True,
    )
    context = {
        'product': product,
    }
    return render(request,
                  'shop/product/detail.html',
                  context)


def main_catalog(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug is not None:
        category = get_list_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category__slug=category_slug)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request,
                  'shop/catalog.html',
                  context)