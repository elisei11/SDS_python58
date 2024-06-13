from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import AddToCartForm
from shop.models import Product


# Create your views here.

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add_to_cart(product=product, quantity=cleaned_data['quantity'], override=cleaned_data['override'])
    return redirect('cart:view_cart')


def view_cart(request):
    cart = Cart(request)
    for product in cart:
        product['update_quantity'] = AddToCartForm(initial={'quantity': product['quantity'], 'override': True})

    return render(request, 'cart/view_cart.html', {'cart': cart})

@require_POST
def update_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        override = form.cleaned_data['override']
        cart.add_to_cart(product=product, quantity=quantity, override=override)
    return redirect('cart:view_cart')

@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove_from_cart(product=product)
    return redirect('cart:view_cart')
