from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from .favorites import Favorites


@require_POST
def add_to_favorites(request, product_id):
    favorites = Favorites(request)
    product = get_object_or_404(Product, pk=product_id)
    favorites.add_to_favorites(product=product)
    return redirect('favorites:view_favorite')


def view_favorites(request):
    favorites = Favorites(request)
    return render(request, 'favorite/view_favorite.html', {'favorites': favorites})


@require_POST
def remove_from_favorites(request, product_id):
    favorites = Favorites(request)
    product = get_object_or_404(Product, pk=product_id)
    favorites.remove_from_favorites(product=product)
    return redirect('favorites:view_favorite')
