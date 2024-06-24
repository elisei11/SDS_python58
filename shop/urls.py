from django.urls import path

from . import views



urlpatterns = [path("", views.HomeView.as_view(), name="homepage"),
               # path('create_category/', views.CategoryCreateView.as_view(), name='create-category'),
               path('category_list/', views.CategoryListView.as_view(), name='category-list'),
               path('product_list/<slug:subcategory_slug>/', views.ListProductView.as_view(), name='product-list'),
               path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),


               path('subcategory_list/<slug:category_slug>/', views.SubCategoryListView.as_view(), name='subcategory-list'),


               ]

app_name = 'shop'
