from django.urls import path

from . import views

urlpatterns = [path("", views.HomeView.as_view(), name="homepage"),
               path('create_category/', views.CategoryCreateView.as_view(), name='create-category'),
               path('category_list/', views.CategoryListView.as_view(), name='category-list'),
               path('product_list/<slug:category_slug>/', views.ListProductView.as_view(), name='product-list'),
               path('product_detail/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product-detail'),
               path('create_customer/', views.CreateCustomerView.as_view(), name='customer-create'),
               ]

app_name = 'shop'
