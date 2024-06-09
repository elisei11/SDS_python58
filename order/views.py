import stripe
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import View

from cart.cart import Cart
from order.forms import OrderForm
from order.models import OrderItem, Order

stripe.api_key = settings.STRIPE_SECRET_KEY

class PlaceOrderView(View):
    def get(self, request, *args, **kwargs):
        form = OrderForm()
        return render(request,'order/place_order.html',{'form':form,"stripe.public_key":settings.STRIPE_PUBLISHABLE_KEY})

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        cart=Cart(request)
        if form.is_valid():
            data = form.cleaned_data
            total_amount = sum(item['price'] * item['quantity'] for item in cart)
            order = Order.objects.create(total_amount=total_amount,user=request.user,**data)
            # order.total_amount = sum(item['price'] * item['quantity'] for item in cart)

            order.user_id = request.user.id

            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item["product"], price=item["price"], quantity=item["quantity"])
            token = request.POST.get('stripeToken')
            charge = stripe.Charge.create(
                amount=int(order.total_amount * 100),
                currency='ron',
                description= f'Order{order.id}',
                source=token,
            )
            if charge['status'] == 'succeeded':
                order.save()
                self.proces_payment(request,order)
                cart.clear()
                return redirect('order_created', order_id=order.id)

        return render(request,'order/place_order.html')

    def proces_payment(self, request,order):
        stripe.api_key=settings.STRIPE_SECRET_KEY
        stripe.api_version="2024-04-10"
        sesion_data={
            "mode": "payment",
            "client_reference_id": order.id,
            "succes_url": request.build_absolute_uri("order:order_created", order.id),
            "cancel_url": request.build_absolute_uri("order:order_created", order.id),
            "line_items": [{"quantity": 1, "price": order.total_amount, "currency": "ron"}],


        }
        sesion=stripe.checkout.Session.create(**sesion_data)
        return redirect(sesion.url, code=303)
class OrderCreate(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'order/order_created.html')





