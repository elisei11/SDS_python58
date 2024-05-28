from django.urls import path

from . import views

urlpatterns = [path("", views.HomeView.as_view(), name="homepage"),
               path('create_category/', views.CategoryCreateView.as_view(), name='create-category'),
               path('category_list/', views.CategoryListView.as_view(), name='category-list'),
               path('product_list/', views.ListProductView.as_view(), name='product-list'),
               ]

app_name = 'shop'
