from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from shop.models import Product, Subcategory


def search_results(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
        subcategories = Subcategory.objects.filter(name__icontains=query)
    else:
        products = Product.objects.none()
        subcategories = Subcategory.objects.none()

    context = {
        'query': query,
        'products': products,
        'subcategories': subcategories,
    }
    return render(request, 'search/search_results.html', context)