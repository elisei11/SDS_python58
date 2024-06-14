import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views.generic import View
from django.urls import reverse
from cart.cart import Cart
from order.forms import OrderForm
from order.models import OrderItem, Order

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views.generic import View
from django.urls import reverse
from cart.cart import Cart
from order.forms import OrderForm
from order.models import OrderItem, Order
from shop.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class PlaceOrderView(View):
    def get(self, request, *args, **kwargs):
        form = OrderForm()
        return render(request, 'order/place_order.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        cart = Cart(request)
        if form.is_valid():
            data = form.cleaned_data
            total_amount = sum(item['price'] * item['quantity'] for item in cart)

            # If user is not authenticated, user will be None
            user = request.user if request.user.is_authenticated else None

            order = Order.objects.create(total_amount=total_amount, user=user, **data)
            order.save()
            for item in cart:
                product = item["product"]
                quantity = item["quantity"]
                OrderItem.objects.create(order=order, product=product, price=item["price"], quantity=quantity)

                # Update product stock
                product.stock -= quantity
                product.save()

            # Create Stripe Checkout Session
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'ron',
                        'product_data': {
                            'name': 'Order {}'.format(order.id),
                        },
                        'unit_amount': int(order.total_amount * 100),  # Stripe expects amount in cents
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('order:order-created', kwargs={'order_id': order.id})
                ),
                cancel_url=request.build_absolute_uri(
                    reverse('order:place-order')
                ),
            )

            # Clear the cart after creating the Stripe session
            cart.clear()

            return redirect(session.url, code=303)
        return render(request, 'order/place_order.html', {'form': form})


class OrderCreate(View):
    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, id=order_id)
        order_items = order.items.all()
        return render(request, 'order/order_created.html', {'order': order,'order_items': order_items})  #
