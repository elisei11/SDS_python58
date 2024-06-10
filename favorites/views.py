from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import DeleteView

from .favorites import Favorites

from shop.models import Product, Favorite


# Create your views here.

@require_POST
def add_to_favorites(request, product_id):
    favorites = Favorites(request)
    product = get_object_or_404(Product, pk=product_id)

    # print(request.POST)
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     cleaned_data = form.cleaned_data
    favorites.add_to_favorites(product=product)
    # print(form.errors)
    return redirect('favorites:view_favorite')


def view_favorites(request):
    favorites = Favorites(request)
    # for product in favorites:
    #     product['update_quantity'] = AddToFavorites(initial={'quantity': product['quantity'], 'override': True})

    return render(request, 'favorite/view_favorite.html', {'favorites': favorites})





@require_POST
def remove_from_favorites(request, product_id):
    favorites = Favorites(request)
    product = get_object_or_404(Product, pk=product_id)
    favorites.remove_from_favorites(product=product)
    return redirect('favorites:view_favorite')
