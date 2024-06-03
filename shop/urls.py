from django.urls import path

from . import views
from .views import CartView

urlpatterns = [path("", views.HomeView.as_view(), name="homepage"),
               path('create_category/', views.CategoryCreateView.as_view(), name='create-category'),
               path('category_list/', views.CategoryListView.as_view(), name='category-list'),
               path('product_list/<slug:category_slug>/', views.ListProductView.as_view(), name='product-list'),
               path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
               path('create_customer/', views.CreateCustomerView.as_view(), name='customer-create'),
               path('cart/', views.CartView.as_view(), name='view_cart'),
               path('add_to_cart/<int:pk>/',views.AddToCartView.as_view(), name='add-to-cart'),
               path('remove_from_cart/<int:pk>/',views.RemoveFromCartView.as_view(), name='remove-from-cart')
               ]

app_name = 'shop'
