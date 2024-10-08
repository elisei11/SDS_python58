from django.urls import path

from order.views import PlaceOrderView, OrderCreate, OrderHistory

urlpatterns = [
    path('place_order/', PlaceOrderView.as_view(), name='place-order'),
    path('order_created/<int:order_id>',OrderCreate.as_view(), name='order-created'),
    path('order_history/', OrderHistory.as_view(), name='order-history'),
]
app_name = 'order'