from django.urls import path

from . import views
from .views import CartView

urlpatterns = [path("", views.HomeView.as_view(), name="homepage"),
               # path('create_category/', views.CategoryCreateView.as_view(), name='create-category'),
               path('category_list/', views.CategoryListView.as_view(), name='category-list'),
               path('product_list/<slug:subcategory_slug>/', views.ListProductView.as_view(), name='product-list'),
               path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
               path('create_customer/', views.CreateCustomerView.as_view(), name='customer-create'),
               path('cart/', views.CartView.as_view(), name='view_cart'),
               path('add_to_cart/<int:pk>/',views.AddToCartView.as_view(), name='add-to-cart'),
               path('remove_from_cart/<int:pk>/',views.RemoveFromCartView.as_view(), name='remove-from-cart'),
               path('subcategory_list/<slug:category_slug>/', views.SubCategoryListView.as_view(), name='subcategory-list'),
               path('add_to_favorite/<int:pk>/', views.AddToFavoriteView.as_view(), name='add-to-favorite'),
               path('favorite/', views.FavoriteView.as_view(), name='view_favorite'),
               path('remove_from_favorite/<int:pk>/',views.RemoveFromFavoriteView.as_view(), name='remove-from-favorite'),

               ]

app_name = 'shop'
