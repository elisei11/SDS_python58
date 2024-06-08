from django.urls import path

from cart import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove-from-cart'),
]

app_name = 'cart'
